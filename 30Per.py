import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import ctypes
import smtplib
from time import ctime
import time
import turtle
import win32api
import win32con
import time
from urllib.request import urlopen
import json
import subprocess
import keyboard
from pynput.mouse import Button, Controller
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am pele Sir. Please tell me how can I help you")

def takeCommand():
    try:
        r = sr.Recognizer()
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        with sr.Microphone() as source:
            print("Listening....")
            r.energy_threshold = 4000
            audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f'You said: {command}')
        except:
            print('Please try again')
            command = takeCommand()
        return command
    except Exception as e:
        print(e)
        return False

def takeGameCommand():
    try:
        r = sr.Recognizer()
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
        with sr.Microphone() as source:
            print("Input for game....")
            r.energy_threshold = 4000
            audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f'You said: {command}')
        except:
            print('Please try again')
            command = takeCommand()
        return command
    except Exception as e:
            print(e)
            return  False



def playGame():
    while True:
        text = takeGameCommand().lower()
        if text == "space":
            pyautogui.keyDown("up")
            time.sleep(1)
            pyautogui.keyUp("space")
        if text == "left jump":
            pyautogui.keyDown("a")
            pyautogui.keyDown("space")
            time.sleep(1)
            pyautogui.keyUp("a")
            pyautogui.KeyUp("space")
        if text == "right":
            pyautogui.keyDown("d")
            time.sleep(1)
            pyautogui.keyUp("d")
        if text == "left":
            pyautogui.keyDown("a")
            time.sleep(1)
            pyautogui.keyUp("a")
        if text == "close":
            print("Game closed")
            return


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.09)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def playAlone():
    webbrowser.open("https://www.agame.com/game/magic-piano-tiles")
    time.sleep(1)
    click(821, 590)
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(535, 590)[0] == 0:
            click(535, 590)
        if pyautogui.pixel(630, 590)[0] == 0:
            click(630, 590)
        if pyautogui.pixel(726, 590)[0] == 0:
            click(726, 590)
        if pyautogui.pixel(821, 590)[0] == 0:
            click(821, 590)



if __name__ == '__main__':

    # wishMe()

    while True:
        query = takeCommand()

    # logic for executing a task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "greet me" in query:
            print(query)
            wishMe()

        elif 'play' in query:
            playGame()

        elif 'airplane' in query:
            playAlone()

        elif 'Good  morning' in query:
            speak("Good morning sir!")

        elif 'Good  afternoon' in query:
            speak("Good afternoon sir!")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open("http://www.google.com/search?q=" + query)

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
            speak("opening Google sir..")

        elif 'about' in query:
            webbrowser.open('http://www.google.com/{query}')

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
            speak("opening youtube sir..")

        elif 'open twitter' in query:
            webbrowser.open('https://twitter.com/explore')
            speak("opening twitter sir..")

        elif 'open linkedin' in query:
            webbrowser.open('https://www.linkedin.com/feed/')
            speak("opening linkedin sir..")

        elif 'open chrome' in query:
            webbrowser.open('http://www.google.com/')
            speak("opening chrome sir..")

        elif 'close tab' in query:
            keyboard.press_and_release('Ctrl + w')
            speak("Done sir")

        elif 'close chrome' in query:
            speak("Closing chrome")
            os.system("taskkill /im chrome.exe /f")

        elif 'how are you' in query:
            speak("I am fine Sir, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you are fine")

        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            speak("opening Gmail sir..")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            speak("opening Gmail sir..")

        elif "who made you" in query or "created you" in query:
            speak = "I have been created by Team Ignite."


        elif 'go back' in query:
            speak('got it')
            keyboard.press_and_release('alt + left arrow')

        elif 'open netflix' in query:
            webbrowser.open('https://netflix.com/')
            print("Opening Netflix sir")
            speak("opening Netflix sir..")

        elif 'open hotstar' in query:
            webbrowser.open('https://www.hotstar.com/in')
            speak("opening hotstar sir..")

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak("opening github sir..")

        elif 'close notepad plus plus' in query:
            keyboard.press_and_release('alt + f4')

        elif 'close notepad' in query:
            keyboard.press_and_release('alt + f4')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir, the time is {strTime}')
            print(strTime)

        elif 'open notepad plus plus' in query:
            speak("There you go sir opening Notepad plus plus..")
            notePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notePath)

        elif 'open notepad' in query:
            NotePath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(NotePath)

        elif 'open report' in query:
            speak("opening your Presentation sir..")
            webbrowser.open(
                "")
            mouse = Controller()
            mouse.position = (1257, 31)
            mouse.click(Button.left, 1)

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on sir, I will show you where " + location + " is.")
            webbrowser.open(
                "http://www.google.nl/maps/place/" + location + "/&amp;")


        elif "what" in query:
            query = query.split(" ")
            location = query[2]+' '+query[3]
            speak("sir According to google " + location + " is.")
            webbrowser.open("http://www.google.com/search?q=" + location)


        elif 'hey jack' in query:
            speak("yes sir")

        elif 'hi jack' in query:
            speak('Hi sir how can i help you!')

        elif 'hello jack' in query:
            speak('Hi sir how can i help you!')

        elif 'jack' in query:
            speak('Hi sir how can i help you!')

        elif 'hey jack can you do me a favour' in query:
            speak('Hi sir how can i help you!')

        elif 'thank you' in query:
            speak('Anytime sir..')
            speak("If you need anything i will be here")

        elif 'open meet' in query:
            speak("ok sir opening google meet")
            webbrowser.open("https://meet.google.com")


        elif "who are you" in query:
            speak("I am your virtual assistant created by team Ignite")

        elif "stop embarrassing me" in query:
            speak("my apologies sir")

        elif "everyone are laughing" in query:
            speak("my apologies sir")

        elif "minimize window" in query:
            speak("ok sir")
            keyboard.press_and_release('command + m')

        elif 'change wallpaper' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:\\Users\\\zig_za\\Downloads\\wallpaper1",
                                                       0)
            speak("Background changed succesfully")


        elif 'revert back to original wallpaper' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:\\Users\\\zig_za\\Downloads\\wallpaper2",
                                                       0)

        elif 'yup good' in query:
            speak("ok sir")

        elif 'log off' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown' in query or 'shut down' in query:
            speak("Hold On sir! Your system is on its way to shut down")
            subprocess.call('shutdown / p /s')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('jack.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(note)
                speak('done sir')
            else:
                file.write(note)

        elif 'wake up' in query:
            speak('online and ready sir')

        elif 'sleep' in query:
            speak('ok sir, i will sleep now')

        elif "quit" in query or "exit" in query:
            speak("going offline sir")
            exit()
