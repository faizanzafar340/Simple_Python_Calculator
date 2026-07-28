def add(a, b):
    return a+b
 

def main():
    
    a = int(input("write no 1: "))
    b = int(input("write no 2: "))
    operation = int(input("1: Add 2: Subtract 3: Multiplicaton 4: Diivision : "))
    if operation == 1:
        print(add(a,b))
    else:
        print("results not found")
    
main() 