#Python Functions Exercise

#Excerise 2, Create a function with variable lenght of arguments

#If we do not know how many arguments will be passed we can add the *args
#See https://www.w3schools.com/python/python_functions.asp for more tips and tricks 

# def func1(*num):
#     for i in num:
#         print(i)

# def main():
#     func1(1,2,3,4,5,6)       
# if __name__ == "__main__":
#     main()   
# Can solve this problem using list slicing 


#Excerise 3, Return multiple values from a function

# def calculation(a,b):
#     add = a+b
#     sub = a-b
        
#     return(add,sub)

# def main():
#     res=calculation(40,10)
#     print(res)       
# if __name__ == "__main__":
#     main()   



# #Excerise 4, Create a function with a default argument

# def showEmployee(name,money = 0):


#     print("Name: ", name,"Salary: ",money)

# def main():

#     showEmployee("Ben", 12000)
#     showEmployee("Jessa")

# if __name__ == "__main__":
#     main()   


#Excerise 5, Create an inner function to calculate the addition in the following way
# SEE why to use inner function for https://realpython.com/inner-functions-what-are-they-good-for/

# from ast import arg


# def func1(a,b):
#     def func2(a,b):
#         return a+b
#     add = func2(a,b)
#     return add +5 
# def main():

#     print(func1(10,20))
    

# if __name__ == "__main__":
#     main()   


#Exercise 6: Create a recursive function
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself, again and again.


def func1(num):
    if num:
        return num + func1(num -1)
    else: 
        return 0

def main():
    
   res = func1(10)
   print(res)
    

if __name__ == "__main__":
    main()   


