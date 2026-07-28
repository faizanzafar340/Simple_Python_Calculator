

import add
from subB import sub
 
def main():
    
    a = int(input("write no 1: "))
    b = int(input("write no 2: "))
    operation = int(input("1: Add 2: Subtract 3: Multiplicaton 4: Diivision : "))
    if operation == 1:
        print(add(a,b))
    elif operation == 2:
        print(sub(a,b))
    else:
        print("results not found") 
    
main() 