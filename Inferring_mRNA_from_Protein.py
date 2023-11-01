# %%
# dictionary of amino acids and how many combinations of bases can make each amino acid.
from functools import reduce
import random

#%%
def generate_random_amino_acids(length=1000):
    amino_acids = [
        "A",
        "R",
        "N",
        "D",
        "C",
        "E",
        "Q",
        "G",
        "H",
        "I",
        "L",
        "K",
        "M",
        "F",
        "P",
        "S",
        "T",
        "W",
        "Y",
        "V",
        "*",
    ]
    max_length = min(length, 1000)
    random_string = "".join(random.choices(amino_acids, k=max_length))
    return random_string


# Example usage
random_sequence = generate_random_amino_acids(length=10)
print(random_sequence)

# %%
amino_acids = {
    "A": 4,  # Alanine
    "R": 6,  # Arginine
    "N": 2,  # Asparagine
    "D": 2,  # Aspartic Acid
    "C": 2,  # Cysteine
    "E": 2,  # Glutamic Acid
    "Q": 2,  # Glutamine
    "G": 4,  # Glycine
    "H": 2,  # Histidine
    "I": 3,  # Isoleucine
    "L": 6,  # Leucine
    "K": 2,  # Lysine
    "M": 1,  # Methionine
    "F": 2,  # Phenylalanine
    "P": 4,  # Proline
    "S": 2,  # Serine
    "T": 4,  # Threonine
    "W": 1,  # Tryptophan
    "Y": 2,  # Tyrosine
    "V": 4,  # Valine
    "*": 3,  # Stop Codon
}


def protein_from_rna(protein_string: list):
    protein_string = protein_string.upper()

    # represent each letter in the aa string by the number of combinations of mRNA bases that could make it
    combination_list = []

    for aa in protein_string:
        if aa in amino_acids:
            value = amino_acids[aa]

            combination_list.append(value)

    possible_mRNA_strings = reduce(lambda x, y: x * y, combination_list)

    modulus = possible_mRNA_strings % 1_000_000

    return modulus


# %%
result = protein_from_rna("MA*")
result
# %%
