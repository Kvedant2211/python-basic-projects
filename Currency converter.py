with open('currency.txt') as f:
    lines = f.readlines()

cdict = {}
for line in lines:
    sp = line.split("\t")
    cdict[sp[0]] = sp[1]

amt=int(input("Enter the amount : \n"))
print("Enter the name that you want to convert this : \n ")
[print(item) for item in cdict.keys()]
currency=input("Please enter one of these value : \n")
print(f"{amt} INR is equal to {amt *float(cdict[currency])} {currency}")

