import random
from re import X



def main():
    
    a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    #look only for even elements in the list use comprehension
    
    even = [x for x in a if x % 2 == 0 ]
    print(even)


if __name__ == "__main__":
    main()