

import add
from subB import sub
import multi
 
def main():
    
    a = int(input("write no 1: "))
    b = int(input("write no 2: "))
    operation = int(input("1: Add 2: Subtract 3: Multiplicaton 4: Diivision : "))
    if operation == 1:
        print(add(a,b))
    elif operation == 2:
        print(sub(a,b))
    elif operation == 3:
        print(multi(a,b))
    else:
        print("results not found") 
    
main() 