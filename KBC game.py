print("KBC game")
print("Welcome to KBC")

ques=[["What is cylinder color?","Orange","Black","Red","Yellow",3],
      ["National fruit of India?","Apple","banana","coconut","mango",4],
      ["Capital of India?","Mumbai","Delhi","Bengluru","Gujrat",2],
      ["Prime minister of India?","Nitin Gadkari","PM Modi","Amit shah","Yogi",2],
      [" Financial capital of India?","Mumbai","Delhi","Bengluru","Gujrat",1],
      ["National animal of India?","Cow","Peacock","Tiger","Lion",3],
      ["Celebration of Republic day India?","15 August","26 Jan","26 August","15 Jan",2],
      ["National river of India?","Kaveri","Godavari","Tapi","Ganga",4],
      ["Number of States in India?","32","28","Other","40",2],
      ["National Tree of India?","Banyan","Tulasi","Mango","ashoka",1]
      ]
level=[1000,2000,3000,4000,5000,10000,25000,50000,75000,100000]
money=0
i=0
for i in range (0,len(ques)):
    que=ques[i]
    print(f"\nQuestion for Rs.{level[i]} is ")
    print(que[0])
    print("Options is..")
    print(f"1. {que[1]}            2. {que[2]}")
    print(f"3. {que[3]}            4. {que[4]}")
    reply=int(input("Enter ans in (1-4) or 0 for Quit "))
    if reply == 0:
        money=level[i]
        print("Thank you !")
        break
    if reply == que[-1]:
        print(f"Correct answer,you have won Rs{level[i]}")
        if (i==4):
            money=5000
        if (i==5):
            money=10000
        elif (i==7):
            money=50000
        elif (i==9):
            money=100000
    else:
        print("Wrong answer \nGood luck next time !") 
        break
print(f"Congragulation ! \nYour winning amount is {money}")  







































'''

i=0
while True:

        print(ques[0])
        len=len(ques)
        print("1.Pink"+"\n2.Green"+"\n3.Red"+"\n4.other")
        n=int(input("Enter ans : "))
        if n==3:
            print("Congragulation!,right answer")
        else:
            print("Wrong answer")
        '''