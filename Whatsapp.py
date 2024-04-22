import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
from Speak import Say

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendMessage():
    Say("Enter the phone Number")
    number = input("Enter Mob. Number:")
    Say("Write your Message here:")
    user_message = input("Message:")
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", user_message)
    Say("Done,sir")

    # #  Approach 2:
    # Say("Who do you want to msg")
    # print("Who do you want to msg")
    # a= int(input('''Person 1-1 Person 2-2'''))
    # if a == 1:
    #     Say("whats the message")
    #     message=str(input("enter the message"))
    #     pywhatkit.sendwhatmsg("+919852213571",message,time_hour=strTime,time_min=update)
    # elif a ==2:
    #     Say("whats the message")
    #     message = str(input("enter the message"))
    #     pywhatkit.sendwhatmsg("+919123192238", message, time_hour=strTime, time_min=update)

