'''
Binary search is the ultimate divide-and-conquer algorithm. To find a key k in a large file containing keys A[1..n] in sorted order, we first compare k with A[n/2], and depending on the result we recurse either on the first half of the file, A[1..n/2], or on the second half, A[n/2+1..n]. The recurrence now is T(n)=T(n/2)+O(1). Plugging into the master theorem (with a=1,b=2,d=0) we get the familiar solution: a running time of just O(logn).
Problem - The problem is to find a given set of keys in a given array:

- Given: Two positive integers n≤10^5 and m≤10^5, a sorted array A[1..n] of integers from −10^5 to 10^5 and a list of m integers 

−10^5 ≤ k1,k2,…,km ≤10^5.

- Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

my notes: 

two potential approaches, iterative and recursive: 

- iterative is O(1) space complexity and O log (N) time complexity - eqiuvalent to creating a pile of boxes, and then if you get a box, you add it to another pile, and if there are more boxes you repeat this process, or if you find a key you're done.

- recursive is O log(n) for both time and space - it's like going through every item in a box, and if you find a box, repeat this, until you find a key


We'll use the iterative binary search function instead. 

'''

#%%
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1

def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        
        if array[mid] < x:
            low = mid + 1
 
        
        elif array[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1

#%% 
#intial test
array = [2, 4, 6, 8, 20, 40, 60, 80]
x = 56

result = binary_search(array, x)

if result != -1:
    print("The index of the element is", int(result + 1))
else:
    print("We do not have this element in the Array.")




#%% test with actual list of integers
integers =  [10,40,35,15,40,20]
array = [10,20,30,40,50]
index_list = []

for integer in integers:
    result = binary_search(array=array, x=integer)
    if result != -1:
        index_list.append(result + 1)
    else:
        index_list.append(result)
    
print(index_list)

#%%