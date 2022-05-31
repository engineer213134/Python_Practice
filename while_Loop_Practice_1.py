import random
from re import X
import secrets
from time import struct_time
from turtle import delay
#Exercise 1: Print First 10 natural numbers using while loop
#def main():  
#    i = 0
#    while(i <= 10):
#        print(i) 
#        i+=1 
#if __name__ == "__main__":
#    main()

#Exercise 2: Print the following pattern
#def main():  
#    for x in range(5):
#        for j in range(1,x + 1):
#            print (j,end=' ')
#        print ("")

#if __name__ == "__main__":
#    main()

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
#def main():
    #User input input
#    input = 3
#    sum = 0 
#    for x in range(1,input + 1 ,1):
#        sum = x + sum  
#    print("The sum is : ",sum)
#if __name__ == "__main__":
#    main()

#Exercise 4: Write a program to print multiplication table of a given number
#def main():
#    mul=2
#    y=0 
#    for x in range(1,10 + 1 ,1):
#        y = mul*x   
#        print(y)
#if __name__ == "__main__":
#    main()

#Exercise 5: Display numbers from a list using loop
#def main():
#    numbers = [12, 75, 150, 180, 145, 525, 50]
    
#    for x in numbers:
#        if x > 150:
#             break
#        elif x > 150: 
#            continue 
#        elif x %5 == 0: 
#            print(x)
#if __name__ == "__main__":
#    main()
   
# Exercise 13 Find the factorial of a given number  
#def main():
    #User input
#    input = 5
#    factoral =1
#    for x in range(1, input+1):
#        factoral = factoral * x 
#        print(factoral)


#    print("The factoral is : " , factoral)

#if __name__ == "__main__":
#    main()   
     
# Exercise 15 Use a loop to display elements from a given list present at odd index positions  
def main():
    #Given list
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for x in my_list :
        index = my_list.index(x)
        if (index%2) != 0:
         print(index)
if __name__ == "__main__":
    main()   
# Can solve this problem using list slicing 

