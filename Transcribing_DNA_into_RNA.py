'''
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
'''

#%%
def DNA_to_RNA(dna_seq:str): 
    dna_seq = dna_seq.upper()
    rna_seq = dna_seq.replace("T", "U")
    print(rna_seq)


#%%
DNA_to_RNA("TGAACGCCAGTTATCGTGACACATTTTGGCTTTCAGAATACTCCGAAATTTACGTAGCTCGACGCAAGCTTAAATCCGATAAGCTAGGACGCGTTAGTCACGACCAAGGACTGTTGGCAGATGAGCCTCACCGAAAATGGACTGGTCTCTACTCGTAAGAGGTCCAGTGTGCTTCGGGTGTCGGTGTGTGCGTAAGAGAAGCCTTAGCGAGATCTCATGCCCAATTTCACTTATAGGTGATTACAATATTAGAGGGAACGTGTCAACAAGCTGAGAGGAAACCTGAATGTTTGACAAAGATCCAACTAATCCCAGATTGCAGGATCAGAGACTAAAGATTTCTGAGCCTTTACACATGACGAAGTAAAAGGGGGGTTGGGGTCAGGAGTCACGGGATCCTTTCCCTTTGGCAGTATGCCGACGGTAGCACAAACAGCCAAAGCAGTTAGTACATAAGACGGGTCATGTAGTGACCTGGTTATCGCCGGTCTGGAGATCATTCAATTTATGATAGTGGGAGACGAACTCGAAGTTATCAAGGGAAGACACGCTAACTAAATACTATGCGTATAAAAAAGGTGAAATGATTTGAAGGTCAAGCGAGTAGTGTCCCAGACATCGGCCGCCTAAATAGAGGTCTCGTGATATTTCTGCTGGGACATTGCAGGACGAGATTTAATTTTAGTAAACGGCTCTAACAGCATTTGTGCTGCCACCTGGTGGGACAAGCATACGGTGCTCTGACTTAAAGCAGGACCGGCCCGGGCAACCGACCCGTACTAGGTACCCTGGAGCGATGGGGACTCACTCGAAACATTTATCCAGGTCGCAGACTAGAGCCTTGACCTAACGGAGGCCACGGCCGACTGCGCGCACCAGCGGGTTCATAGTCAATTCTGTTCCCTCCTGGACGAATAGGTCGAGAGAGTTGAGGCGCCCGCAAGAAAATAATCGGAGCGTTTGCTGTGATGTGAGAAGGCTCTCTCACAGCGTGGT")
# %%
