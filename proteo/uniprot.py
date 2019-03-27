import requests
from proteo.exceptions import ProteinNotFoundError


class UniprotClient(object):
    """
    Proteo UniProt Client
    """
    def __init__(self):
        """
        Initializes the UniProt client.

        The UniProt API supports XML and FASTA endpoints, but XML payloads
        are significantly larger. FASTA is preferred here to reduce overhead.
        """
        self.fasta_url = "https://www.uniprot.org/uniprot/{0}.fasta"
        self.xml_url = "https://www.uniprot.org/uniprot/{0}.xml"

    def get_protein(self, protein_id):
        """
        Returns a dictionary of protein data given a valid UniProt ID
        """
        protein_url = self.fasta_url.format(protein_id)
        response = requests.get(protein_url)
        
        if response.encoding == 'ISO-8859-1':
            # Valid response content with protein data
            fasta_text = response.text.strip()
            protein_dict = self.__parse_fasta(fasta_text)

            return protein_dict
        else:
            # 'Not Found' response is a UTF-8 encoded HTML page
            msg = "Protein ID {0} not found".format(protein_id)
            raise ProteinNotFoundError(msg)

    def __parse_fasta(self, fasta_text):
        """
        Extracts protein data from a FASTA response and returns it in a dict
        """
        protein = {}
        protein['sequence'] = ""

        if fasta_text:
            lines = fasta_text.split('\n')
            for line in lines:
                if line[0] == '>':
                    # Protein Meta info
                    meta = line.split(" ")
                    short_labels = meta[0].split("|")
                    protein['primary_accession_number'] = short_labels[1]
                    protein['name'] = short_labels[2]
                    protein['gene'] = self.__split_tag(meta[-3])
                    protein['taxonomic_id'] = self.__split_tag(meta[-4])
                    del meta[0]
                    del meta[-4:]

                    org_index = -1
                    for i, chunk in enumerate(meta):
                        if chunk[0:2] == 'OS':
                            org_index = i
                    
                    protein['organism'] = self.__split_tag(
                        tagged_value=' '.join(meta[org_index:])
                    )
                    protein['recommended_name'] = ' '.join(meta[0:org_index])

                else:
                    # Lines of sequence data
                    protein['sequence'] += line

        return protein

    def __split_tag(self, tagged_value):
        """
        Returns just the cleaned value for a tagged piece of meta info
        """
        return tagged_value.split("=")[-1]
