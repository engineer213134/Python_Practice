
#Python Data Structure Exercise for Beginners
#Lists,Sets,Dictonary,Tuple


#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second


# def main():
#     l1 = [3, 6, 9, 12, 15, 18, 21]
#     l2 = [4, 8, 12, 16, 20, 24, 28]
#     #Create list l3 to hold the found numbers 
#     l3 = []
#     # #Read the first list use a for loop and an if statment
#     # for x in l1:
#     #     if x%2==1:
#     #        l3.append(x)
#     # print(l3)
    
#     #Using concatination to merge lists and find even and odd numbers 
#     l4 = l1+l2
#     for x in l4:
#         if l4.index(x)%2==1:
#             l3.append(l4.index(x))
#         else:
#             l3.append(l4.index(x))
#         print(l4.index(x))        

#     for index, value in enumerate(l4):
#         print(index)  
    

# if __name__ == "__main__":
#     main()   

#Exercise 2: Remove and add item in a list Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.


# def main():
#     l1 = [3, 6, 9, 12, 15, 18, 21]
#     #Using the pop() method to remove item at index 4 
#     print("Before Switch: ",l1)
#     l1.insert(2,l1.pop(4))
#     #Insert the number at index 2
#     print("After Switch: ", l1)
# if __name__ == "__main__":
#     main()   


# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# def main():
#     l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#     Use slicing 
#     print("After Slice: ", l1[0:3])
#     print("Reverse List slice: ", l1[-7:-10:-1])

#     for x in l1: 
#         l1/3

   
# if __name__ == "__main__":
#     main()   


#Exercise 4: Count the occurrence of each element from a list ,Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

# def main():
#     sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#     #This is setting the variable vested as false for all list elements 
#     visted = [False for x in range(len(sample_list))]
#     #loop over the list see https://www.geeksforgeeks.org/python-boolean-list-initialization/ for list comprehension 
#     for x in range(len(sample_list)):
#         #A simple solution is to run two loops. For every item count number of times, it occurs. To avoid duplicate printing, keep track of processed items. 
#         if (visted[x] == True):
#             continue
#         #Loop for counting Frequency
#         count = 1
#         for j in range(x+1,len(sample_list),1): 
#             if (sample_list[x] == sample_list[j]):
#                 visted[j] == True
#                 count += 1
#         print(sample_list[x],count)

#     #Same Problem using hashing and dictonarys 
#     mp=dict()
#     # Traverse through array elements
#     # and count frequencies
#     for i in range(len(sample_list)):
#         if sample_list[i] in mp.keys():
#             mp[sample_list[i]] += 1
#         else:
#             mp[sample_list[i]] = 1
#     # Traverse through map and print
#     # frequencies
#     for r in mp:
#         print(r, " ", mp[r])

# if __name__ == "__main__":
#      main()   


# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# def main():
#     roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
#     #Define a dictornary called sample_dict
#     sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
  
#     #Take the roll_number list and compare to the dictonary sample_dict
#     #Loop through dict using conditional list comprehension SEE https://www.programiz.com/python-programming/list-comprehension
#     #Note data is an object and we print it 
#     data = [k for k, v in sample_dict.items() if v in roll_number]
#     print(data)
# if __name__ == "__main__":
#     main()   


#Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
#Info on tuples https://www.w3schools.com/python/python_tuples.asp
#Info on finding duplicates https://www.techiedelight.com/find-duplicate-items-python-list/
# def main():
#     sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#     #Look for duplicats in a list
#     visted = set()
#     number_list = [ x for x in sample_list if x in visted or (visted.add(x) or False)]
#     print("These are the duplicated numbers :",number_list)
# if __name__ == "__main__":
#     main()   

