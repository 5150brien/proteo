# Proteo

A simple Python library for working with UniProt, the *Universal Protein resource*.

## Usage

```python
from proteo.uniprot import UniprotClient

# Initialize a client
u = UniprotClient()

# Use the get_protein method to retrieve a protein record by accession number
accession_number = "B5ZC00"
response = u.get_protein(accession_number)

# Protein data is returned as a dictionary
print(response['gene'])
#glyQS

print(response['name'])
#SYG_UREU1

print(response['organism'])
#Ureaplasma urealyticum serovar 10 (strain ATCC 33699 / Western)

print(response['primary_accession_number'])
#B5ZC00

print(response['recommended_name'])
#Glycine--tRNA ligase

print(response['sequence'])
#MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK
```

## Exceptions

If the get_protein method is called with an invalid accession number, it will raise proteo.exceptions.ProteinNotFoundError
