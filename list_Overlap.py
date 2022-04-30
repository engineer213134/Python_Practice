import random
from re import X

def difference (list1, list2):
    #Single line for python for loop this is a list compehension line below
    #See https://www.youtube.com/watch?v=9qsq2Vf48W8&t=300s for explination 
    #See https://blog.finxter.com/list-comprehension/
    # lst = [<expression> for <item> in <collection> if <expression>] 
   list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return list_dif

def main():
    #Generate random lists 
    random_List1= random.sample(range(1,100),5)
    random_List2= random.sample(range(1,100),7)
    #compare both lists and save common elements in a common list
    z = difference (random_List1, random_List2)
    print("Difference of first and second String: " + str(z))

if __name__ == "__main__":
    main()