def add():
    n1=int(input("Enter number1 ="))
    n2=int(input("Enter number2 ="))
    ans=n1+n2
    print("Addition is =",ans)

def sub():
    n1=int(input("Enter number1 ="))
    n2=int(input("Enter number2 ="))
    ans=n1-n2
    print("Subtraction is =",ans)

def mul():
    n1=int(input("Enter number1 ="))
    n2=int(input("Enter number2 ="))
    ans=n1*n2
    print("Multiplication is =",ans)

def div():
    n1=int(input("Enter number1 ="))
    n2=int(input("Enter number2 ="))
    if n2!=0:
        ans=n1//n2
        print("Division is =",ans)    
    else:
        print(" Error: Can't divide by zero")  

def menu():
    print("Menu")  
    print("1. Addition")  
    print("2. Subtraction")  
    print("3. Multiplication") 
    print("4. Division")  
    print("5. Exit")  

while(True):
    menu()
    c=int(input("Enter choice ="))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()
    elif c==4:
        div()
    elif c==5:
        print("Done")
        break
    else:
        print("Wrong input")
        
    
    
