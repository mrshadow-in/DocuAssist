# Function
import datetime
import webbrowser
import sys

# sys.path.append('i:\Xite development\JARVIS 2.0\Body')
from Body.speak import Speak
import urllib


# 2 Types

# 1 - Non Input
# eg: Time , Date , Speedtest

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    Speak(time)


def Date():
    date = datetime.date.today()
    Speak(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak(day)


def yt():
    webbrowser.open(url='https://youtube.com')


def facebook():
    webbrowser.open(url='https://facebook.com')


def xite():
    webbrowser.open(url='https://xitenodes.com')


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "yt" in query:
        yt()

    elif "youtube" in query:
        yt()

    elif "fb" in query:
        facebook()

    elif "facebook" in query:
        facebook()


# 2 - Input
# eg - google search , wikipedia

def InputExecution(tag, query):
    if "play" in tag:
        name = str(query).replace("play", "")
        import pywhatkit
        pywhatkit.playonyt(query)
