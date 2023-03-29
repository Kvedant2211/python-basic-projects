print("Welcome to Robo Speaker \n-Enter q for end")
from win32com.client import Dispatch
while True:
    speak = Dispatch("SAPI.SpVoice").Speak
    x = input("Enter what you want me to speak : ")
    if x=="q":
        break
    speak(f"{x}")
print("Thank you for using robo speaker")