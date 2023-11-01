# Problem 28: Introduction to Random Strings

# Given: A DNA string ss of length at most 100 bp and an array AA containing at most 20 numbers between 0 and 1.

# Return: an array B having the same length as AA in which B[k] represents the log10(probability) that a random DNA string constructed with the GC-content with same GC content as A[i] will match the strings GC content excatly


#solution: Lets say we have a GC content of 0.129 (12.9 percent) and a string, ACTGA. What we are asking, is that, given that we expect a GC content of 12.9%, how likely is it for this string to occur, and then take it's -log 10 probability. Remembering that the chance of G or C is GC_content/2 and for AT is 1-GC_content/2

# the math would be -log10( 1-0.129/2 * 0.129/2 * 1-0.129/2 * 1-0.129/2 * 0.129/2) 

#this is where the log10(x * y) = log10(x) + log10(y) becomes useful, as it means we can simply get the cumulative sum of the log as you iterate through your string shown below. 


# %%
import math


def RandomString(random_dna_string: str, numeric_array_A: list):
    random_dna_string = random_dna_string.upper()

    at = random_dna_string.count("A") + random_dna_string.count("T")
    gc = random_dna_string.count("C") + random_dna_string.count("G")

    numeric_array_B = []

    for i in range(0, len(numeric_array_A)):
        # number of gc in string * log10(gc content in array/ 2 ) + number of at in string * log10((1-gc content_array)/ 2 )

        prob = gc * math.log10(numeric_array_A[i] / 2) + at * math.log10(
            (1 - numeric_array_A[i]) / 2
        )

        numeric_array_B.append(prob)

    return numeric_array_B


# %%
result = RandomString("ATGC", [0.4])
result

# %%
