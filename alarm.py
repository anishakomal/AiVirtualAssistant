'''
#Function
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm1.py")
      
    
     
    elif "set an alarm" in query:
            print("input time example:- 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :-")
            alarm(a)
            speak("Done,sir")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            # speak(f"Sir,the time is {strTime}")
'''

import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Data.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Data.txt","r+")
deletetime.truncate(0)
deletetime.close()

 

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("notification.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)