
import requests
import json
print("Welcome to whether app")
city=input("Enter city name : ")

url=f"https://api.weatherapi.com/v1/current.json?key=a9528e984d4a4db780b152705232803&q={city}" #url take from whetherapi.com as example

r=requests.get(url)
#print(r.text)
wdict=json.loads(r.text)

from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak
temp=wdict["current"]["temp_c"]#here we want tmp from current inside temp_c in above url
time=wdict["location"]["localtime"]
speak(f"temperature of {city} is {temp}")
print("Temperature",temp)
print("Time",time)