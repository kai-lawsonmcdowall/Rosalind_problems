#%%
import random 
#%% 
#generates our DNA string. 
def DNA(length):
    return ''.join(random.choice('CGTA') for _ in range(length))

#%%
# Generating a random FASTA file with: 
# Length of sequences, l,  between 5 and 50. 
# Number of sequences, N, between 100 and 1000. 

def fasta_file_generator(path_to_file:str, length:int=25, number_of_entries:int = 500):
    
    f = open(path_to_file, "w")
    for i in range(number_of_entries):
        DNA_string = DNA(length)
        f.write(f">Rosalind_{i+1}\n")
        f.write(f"{DNA_string}\n")
    f.close()

#%%
#fasta_file_generator("/home/kai/Rosalind_problems/test.fasta", number_of_entries=10)