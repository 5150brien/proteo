import unittest
from proteo.uniprot import UniprotClient
from proteo.exceptions import ProteinNotFoundError


class TestUniprotClient(unittest.TestCase):
    """
    Tests the UniprotClient class
    """
    def setUp(self):
        self.valid_id = "B5ZC00"
        self.invalid_id = "BA0123456789AB"
        self.u = UniprotClient()

    def test_invalid_accession_id(self):
        """
        Invalid IDs should raise ProteinNotFoundError
        """
        with self.assertRaises(ProteinNotFoundError):
            self.u.get_protein(self.invalid_id)

    def test_valid_return(self):
        """
        Valid IDs should return a dict of non-empty strings
        """
        protein_data = self.u.get_protein(self.valid_id)
        self.assertIs(type(protein_data), dict)

        for key, val in protein_data.items():
            self.assertIs(type(val), str)
            self.assertTrue(val)
