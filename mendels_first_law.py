#%%
"""
Introduction to Mendelian Inheritance

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
- k individuals are homozygous dominant for a factor, 
- m are heterozygous, 
- n are homozygous recessive.


"""

#%%
import random
from math import comb


#%% 

def mendelian_inheritance(k:int = None, 
                          m:int = None,
                          n:int = None):
    


    #for the sake of argument, have between 0 and 10 each
    if k==None:
        k = random.randint(0,10)
    if m==None:  
        m = random.randint(0,10)
    if n==None:
        n = random.randint(0,10)
   

    print(f'homozygous dominant: {k}')
    print(f'heterozygous dominant: {m}')
    print(f'homozygous recessive: {n}')


    """
    6 possible combinations (0 - 0% chance of dominance, 1, 100% chance): 
    - k + k = 1
    - k + m = 1
    - k + n = 1
    - m + m = 0.75
    - m + n = 0.5
    - n + n = 0 

    so possible dominant is 
    """

    #combinationf formula, where we find out how many potential combinations there, as we are interested in pairs, we do nCr, of total indviduals and then 2
    #e.g., k = 2, m = 2, n =2, would be 90. as nCr = nCr = n! / r!(n-r)! =  6! / 2!2!2!(6-2-2-2)!
    #total population and all their potential offspring.
    total_individuals = k + m + n
    possible_combinations_of_mates =comb(total_individuals,2)
    print(f'possible combinations: {possible_combinations_of_mates}')

    #represent the math above.
    total_heterozgyous_dominant = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    print(f'possible heterozygous_combinations:{round(total_heterozgyous_dominant)}')

    print(f'probability of heterozygous offspring: {total_heterozgyous_dominant/possible_combinations_of_mates}')
