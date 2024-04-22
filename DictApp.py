import os
import pyautogui
import webbrowser
import subprocess
from Speak import Say

from time import sleep



# dictapp = {
#     "commandprompt": "cmd",
#     "paint": "paint",
#     "word": "winword",
#     "excel": "excel",
#     "chrome": "chrome",
#     "vscode": "code",
#     "powerpoint": "powerpnt"
# }
dictapp = [
    ['paint', 'mspaint.exe'],
    ["command prompt", "cmd.exe"],
    ['word', 'word'],
    ['notepad', 'notepad.exe'],
    ["excel", "excel"],
    ['calculator', "calc.exe"],
    ['File explorer', 'explorer.exe'],
    ["chrome", "chrome.exe"],
    ["vs code", "Code.exe"],
    ["powerpoint", "powerpnt.exe"],
    ['vlc','vlc']
]

sites = [
    ["youtube", "youtube.com"],
    ["facebook", "facebook.com"],
    ["udemy", "udemy.com"],
    ["instagram", "instagram.com"],

]

def openappweb(query):
    Say("Launching,sir")


    for site in sites:
        if f"open {site[0]}".lower() in query:
            Say(f"opening {site[0]}")
            webbrowser.open(site[1])

    for app in dictapp:
        if f"open {app[0]}".lower() in query:
            Say(f"opening {app[0]}")
            subprocess.Popen(app[1])

    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")



def closeappweb(query):
    Say("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")


