# Proteo

A simple Python library for working with UniProt, the *Universal Protein resource*.

## Installation

```
pip install proteo
```

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

print(response['recommended_name'])
#Glycine--tRNA ligase

print(response['sequence'])
#MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK
```

## Response Dictionary

The protein response dictionary contains the following items:

Key | Meaning
------------ | -------------
gene | The gene coding the protein
name | The protein's short name
organism | The organism in which the protein is found
primary_accession_number | The protein's UniProt accession number
recommended_name | The protein's long/recommended name
sequence | The amino acid sequence defining the protein

## Exceptions

Proteo defines the following exceptions:

Exception | Meaning
------------ | -------------
proteo.exceptions.ProteinNotFoundError | Raised when no protein can be found for the accession number that was provided.

