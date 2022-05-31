
#Python Data Structure Exercise for Beginners
#Lists,Sets,Dictonary,Tuple


#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second


def main():
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    #Create list l3 to hold the found numbers 
    l3 = []
    # #Read the first list use a for loop and an if statment
    # for x in l1:
    #     if x%2==1:
    #        l3.append(x)
    # print(l3)
    
    #Using concatination to merge lists and find even and odd numbers 
    l4 = l1+l2
    for x in l4:
        if l4.index(x)%2==1:
            l3.append(l4.index(x))
        else:
            l3.append(l4.index(x))
        print(l4.index(x))        

    for index, value in enumerate(l4):
        print(index)  
    

if __name__ == "__main__":
    main()   

