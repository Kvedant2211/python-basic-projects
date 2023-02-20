#Secrete code Language

print("Welcome \n-----Secrete code Language-----")
str=input("Enter message = ")   
words=str.split(" ")
coding=input("Enter number \n1.coding \n2.Decoding = ")

coding  =True if(coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="rui"
            r2="dsu"
            nstr=r1 + word[1:] + word[0] +r2
            nwords.append(nstr)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="rui"
            r2="dsu"                     
            nstr=word[3:-3] 
            nstr=nstr[-1] + nstr[:-1]
            nwords.append(nstr)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

'''
#code for random string generating of given length
import string 
import random
l=3
r1=''.join(random.choices(string.ascii_lowercase,k=l))
r2=''.join(random.choices(string.ascii_lowercase,k=l))
print(str(r1))
print(str(r2))


'''