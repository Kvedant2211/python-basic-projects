

import time
th=int(time.strftime("%H"))
print(th)
tm=int(time.strftime("%M"))
print(tm)
ts=int(time.strftime("%S"))
print(ts)
if th >=5 and th< 11:
    print("Good morning"+"\n***Take Breakfast***")
elif (th >=12 and th<16):
            print("Good Afternoon "+"\n***Take lunch***")
elif (th>=17 and th<22):
            print("Good Evening"+"\n***Take Tea***")
elif (th>=22 and th<=24):
            print("Good Night"+"\n***Take Sleep***")
else:
    print("Thank you")   