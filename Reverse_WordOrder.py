import random
from re import X

#Reverse String function
def reverse_string(usr_in):
    reverse_string_list = usr_in[slice(None,None,-1)]
    return reverse_string_list

def main():
    
    #users input of string
    usr_in = input("Enter a string and I will reverse : ")
    #Reverse string of charerters use a function
    print ("\nAfter reverse string function : ", reverse_string(usr_in))
    print("\nBefore string was reversed : ",usr_in)
     




   


if __name__ == "__main__":
    main()