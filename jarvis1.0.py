import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import json
from requests import get
from urllib.request import urlopen
import wolframalpha
import time
import cv2
import pywhatkit

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

wolframalpha_app_id = 'RXYKRX-ELWU4E4K4X'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12 Hour clock
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Vikash!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night") 

    speak("I am Jarvis Please tell me how can I help you, Sir")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/GIITSSS/Desktop/screenshot.png')
    speak("Screenshot has Captured")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def joke():
    joke_ = pyjokes.get_joke()
    print(joke_)
    speak(joke_)


if __name__ == "__main__":
    wishme()
    while True:
        query = TakeCommand().lower()
        if 'time now' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Users/GIITSSS/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'notepad' in query:
            npath = "C:/Windows/system32/notepad.exe"
            os.startfile(npath)
        
        elif 'command' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break

        elif 'how are you' in query:
            speak("I am fine, Sir thanks for asking. How are you sir, i hope you get well soon.")

        elif 'hello' in query:
            speak("Hi, How are you sir ")    

        elif 'creator' in query or 'vikash' in query or 'vikas' in query:
            speak("Vikash is a nice guy , Currently he is studing Computer Science at Motihaari college of Engineering")    

        elif 'who are you' in query or 'yourself' in query or 'your name' in query:
            speak("I am Jarvis 1.0 personal AI assistant, i am created by Vikash, i can help you in various regards, I can search for you on the Internet,I can also play on Youtube, I can also grab information from wikipedia, i can try to make your life better, you just have to command me and I will Do for you.")    

        elif 'who am' in query:
            speak("If you can Talk then definately you are a Human")            

        elif 'youtube' in query:
            speak("What should I play on Youtube?")
            ytvd = TakeCommand()
            pywhatkit.playonyt(ytvd)

        elif 'on google' in query:
            speak("What should I search on Google?")
            search_Term = TakeCommand().lower()
            speak("Searching....")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'offline' in query:
            speak("Going Offline Sir! have a good day")
            quit()

        elif 'love' in query:
            print("Love is our 7th sense that destroys all 6 other sense And makes the person nonsense .")
            speak("Love is our 7th sense that destroys all 6 other sense And makes the person nonsense .")

        elif 'word' in query:
            speak("Opening MS Word...")
            ms_word = r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Word 2010'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I write, Sir?")
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak("Sir should I include Date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes Sir!")
            else:
                file.write(notes)

        elif 'notes' in query:
            file = open('notes.txt', 'r')
            print(notes)
            speak(notes)

        elif 'screenshot' in query:
            screenshot()

        elif 'play song' in query or 'play music' in query:
            song_dir = 'G:/All songs/All songs'
            music = os.listdir(song_dir)
            speak("What should I play?")
            speak("Select a number...")
            ans = TakeCommand().lower()
            while 'number' not in ans:
                speak("I couldnot understand you Please try again!")
                ans = TakeCommand().lower()
            no = int(ans.replace('number', ''))
            os.startfile(os.path.join(song_dir, music[no]))

        elif 'remember that' in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember' in query:
            remember = open('memory.txt', 'r')
            speak("Yes I can remeber"+remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8e41b7d2b37d420e91f725536961730f")
                data = json.load(jsonObj)
                i = 1
                speak("Here are some Headlines from the Entertainment Industry")
                print("========== TOP HEADLINES =========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            speak("User asked to Locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is : '+answer)
            speak('The Answer is'+answer)

        elif 'what is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results!")    

        elif 'listening' in query or 'listen' in query:
            speak("For how many second you want me to stop listening?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'ip' in query:
            ip = get('https://api.ipify.org/').text
            speak("Your IP address is"+ip)