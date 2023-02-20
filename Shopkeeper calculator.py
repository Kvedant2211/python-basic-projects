print("Welcome to White magic store")
sum = 0
while(True):
    userinput=input("Enter item price or  press q to quit : \n")
    if userinput !='q':
        sum=sum+int(userinput)
        print(f"Your order total so far is Rs.{sum}")
    else:
        print(f"Your Bill total is Rs.{sum} \n Thanks for shopping with us ")
        break

