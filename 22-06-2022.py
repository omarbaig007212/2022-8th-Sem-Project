from email import message
from tkinter import messagebox
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
import win32api
import win32con
import time
from urllib.request import urlopen
import subprocess
import keyboard
from pynput.mouse import Button, Controller
import pyautogui
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
from email import message
from tkinter import messagebox



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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


def sendEmail(to, contents):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('180511.cs@hkbk.edu.in', 'ROBOMATE')
    server.sendmail('omarbaig918@gmail.com', to, contents)
    server.close()


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
        return False

class LoginPage:
    def __init__(self, window):

        def validateLogin(username, password):
                print("username entered :", username.get())
                print("password entered :", password.get())
                if (username.get() == 'ignite' and password.get() == 'ignite'):
                    messagebox.showinfo("","Welcome 'Team Ignite'")
                    window.destroy()
                    Widget()
                        
                elif (username!="ignite" and password != "ignite"):
                    messagebox.showinfo("","Wrong Username or Password")
                    return


        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Ignite')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        ##
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        ##
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)


        ##
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)


        ##
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)


        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))

        ##
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        username = self.username_entry

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        #
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        
        ##
       
       
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))

        ##
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)
        password = self.password_entry
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        #
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        #
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)



        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)

        validateLogin = partial(validateLogin, username, password)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=validateLogin)
        self.login.place(x=20, y=10)
       
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

class Widget:  
    def __init__(self):
        self.main()
    def main(self):
        root = Tk()
        root.title('Ignite')
        root.geometry('520x320')
        # img = ImageTk.PhotoImage(Image.open('1.jpg'))
        panel = Label(root)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(
            root, text='ignite', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        compFrame = LabelFrame(root, text="Ignite", font=('Railways',10, 'bold'))
        compFrame.pack(fill="both", expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
                     bg='red', fg='white', command=self.start).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow',
                      fg='black', command=root.destroy).pack(fill='x', expand='no')
        speak('Welcome team Ignite!')
        root.mainloop()

    def start(self):
        while True:
            query = takeCommand()

            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", " ")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    contents = takeCommand()
                    speak("whome should i send")
                    to = "yaseenproduction17045@gmail.com"
                    # to  = "wmohammed693@gmail.com"
                    sendEmail(to, contents)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'play music' in query:
                music_dir = 'C:\\Users\\zig_za\\Music\\music'
                songs = os.listdir(music_dir)
                speak("There you go sir.. playing your favourite")
                os.startfile(os.path.join(music_dir, songs[0]))
            
            elif "greet me" in query:
                print(query)
                wishMe()

            elif 'game' in query:
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
                speak("opening chrome sir..")
                webbrowser.open('http://www.google.com/')

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

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Team Ignite.")

            elif "introduce our team" in query or "introduce" in query:
                speak(
                    "We are team Ignite , Our team guide is Smitha Kurian , Team members are ")
                speak("Ameen")
                speak("Kushal")
                speak("Mirza")
                speak("Lakshan")

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

            elif 'close application' in query:
                keyboard.press_and_release('alt + f4')
                speak("Closing the application")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f'sir, the time is {strTime}')
                print(strTime)

            elif 'open notepad plus plus' in query:
                speak("There you go sir opening Notepad plus plus..")
                notePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(notePath)

            elif 'open notepad' in query:
                speak("Opening notepad")
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
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                                           0,
                                                           "C:\\Users\\\zig_za\\Downloads\\wallpaper2.jpg",
                                                           0)
                speak("Background changed succesfully")

            elif 'original wallpaper' in query:
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
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
                os.system('shutdown -s')

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

if __name__== '__main__':
    page()