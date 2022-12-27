'''
As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly.

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:

s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

'''
#%%
import random
from Bio.Seq import Seq
from scipy.spatial.distance import hamming

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

#%%
#read in as dictionary where header is key and sequence is value
with open("/home/kai/Rosalind_problems/test.fasta") as f:
    fasta_dictionary = {line.strip():next(f).strip() for line in f}

#%%
#generate reverse complements
rev_dict_keys = []
rev_dict_values = []

for fasta_key,fasta_value in fasta_dictionary.items():
    seq = Seq(fasta_value)

    reversed_key = str(fasta_key) + "_rev"
    reversed_value = str(seq.reverse_complement())

    rev_dict_keys.append(reversed_key)
    rev_dict_values.append(reversed_value)

#create dictionary with reverse complement fasta sequences:
rev_fasta_dictionary = {rev_dict_keys[i]: rev_dict_values[i] for i in range(len(rev_dict_keys))}

#%%
#merge the original and it's reverse complements.
complete_fasta_dictionary = dict(fasta_dictionary, **rev_fasta_dictionary)

#%%
#non-complement pair - > two pairs
#complement pair -> two pairs.
#non-complement pair -> still alone. 


#%%
#check if two values are the same by flipping dictionary: 
flipped_fasta_dictionary = {} 
for key, value in complete_fasta_dictionary.items():
    if value not in flipped_fasta_dictionary:
        flipped_fasta_dictionary[value] = [key]
    else:
        flipped_fasta_dictionary[value].append(key)
print("duplicates", str(flipped_fasta_dictionary))

#%%
#extract correct reads. 
correct_reads = {}
for k, v in flipped_fasta_dictionary.items():
    if len(v)>=2:
        correct_reads[k] = v
print(correct_reads)

#%%
#compare all values that aren't paired with all the paired values. 
#return those with a distance of exactly 1 to one of the pairs. 
potentially_incorrect_reads = {k: v for k, v in flipped_fasta_dictionary.items() if k not in correct_reads}

#%%
print(potentially_incorrect_reads)
#%%
#removing complements of potentially incorrect sequences now we don't need them
for k, v in potentially_incorrect_reads.items(): 
    if "rev" in v:
        del potentially_incorrect_reads

#%%
for incorrect_sequence_keys, incorrect_sequence_values  in potentially_incorrect_reads.items(): 
    for correct_sequence_keys, correct_sequence_values in correct_reads.items():
        
        count = sum(1 for a, b in zip(incorrect_sequence_keys, correct_sequence_keys) if a != b)
        
        if count == 1:
            print(f'incorrect entry: {incorrect_sequence_values} matches correct entry {correct_sequence_values}')
            print(f'{incorrect_sequence_keys} -> {correct_sequence_keys}')

#%%

