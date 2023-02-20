# Exercise 1->  d7
# Exercise 1 solution-> d8

print("....Create calculator.... \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
a=int(input("Enter 1st number = "))
b=int(input("Enter 2nd number = "))
c=int(input("Enter number for choice ="))

def cal(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a//b
sum=cal(a,b,c)
sub=cal(a,b,c)
mul=cal(a,b,c)
div=cal(a,b,c)
print(sum)
print(sub)
print(mul)
print(div)




# a=2
# b=4
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# mod=a%b
# sqr=a**b
# print("\nADD",add,"\nSUB",sub,"\nMUL",mul,"\nDIV",div,"\nMOD",mod,"\nSQR",sqr)
# print("The value of",a ,"//",3, "is=", a//b)

