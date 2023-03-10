#Write a Python function that takes in a list of integers and returns the
#length of the longest increasing subsequence (LIS). A subsequence is a
#sequence that can be derived from the original sequence by deleting some elements 
#without changing the order of the remaining elements. 
#An increasing subsequence is a subsequence in which the elements are in increasing order.

#Input list
seq = [10, 9, 2, 5, 3, 7, 101, 18] 
#Create list same size as input list initlize to 1's
dq = [1] * len(seq)

#iterate over seq list compare values
for i in range (len(seq)):
    for j in range(len(seq)):
        if  seq[j] < seq[i]:
           dq[i] = max(dq[i],dq[j]+1)
            
print(max(dq))
