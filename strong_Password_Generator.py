import random
from re import X
import secrets

#A program to generate a random 32-bit string 

#create pass word function
def pass_word():
    secure_pass= secrets.token_hex(32)
    print("Your Secure 32-bit Password is", secure_pass)
    #Send secure token to a text file
    f=open('/home/computer/Desktop/password.txt','w')
    f.write(secure_pass)

def main():    
    #Ask user if they want a strong password Y or n input
    usr_in = input("Would You Like A Strong Password ?  [Y/n] : ")
    if (usr_in == "Y"):
        #call the create pass_word function
         pass_word()
    elif (usr_in == "n"):
            print("Ok No Secure Password For You !!!!!!!")
if __name__ == "__main__":
    main()



   
     


