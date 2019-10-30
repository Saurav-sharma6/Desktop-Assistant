import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import pyaudio
import webbrowser
import os
import random
from os import system
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    speak(f"Good Morning Saurav  i am a Chitti! Cpu speed is 1 Peta Byte 24 seconds clock ")
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak(f"Its {hour}A.M in Morning")
    elif hour >=12 and hour <18:
        speak(f" Its {hour}P.M  in Afternoon")
    else :
        speak(f" Its {hour}P.M ")
    speak("How may i help you!")




def takecommand():
    #takes input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        #print(f"User said: {query.upper()}\n ")
    except Exception as e:
        #print(e)
        print("PLease Say that again...")
        return "none"
    return query
flag=1

if __name__=='__main__':
    wishme()
    while flag==1:
     query = takecommand().lower()
     if 'wikipedia' in query:
         print("Searching Wikipedia...")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         print(results)
         speak(f"According to wikipedia{results}\n")
     elif "open youtube" in query:
         webbrowser.open('youtube.com')
     elif "open instagram" in query:
         webbrowser.open('instagram.com')
     elif "open stackoverflow" in query:
         webbrowser.open('stackoverflow.com')
     elif "open google" in query:
         webbrowser.open('google.com')
     elif "play music" in query:
         music_dir = 'E:\\Local F\\my music'
         songs = os.listdir(music_dir)
         lenght = len(songs)
         print(songs, lenght)
         os.startfile(os.path.join(music_dir, songs[random.randint(0,lenght-1)]))
     elif  "time " in query:
         strtime=datetime.datetime.now().strftime("%H hours %M minutes%S seconds")
         speak(f"Time is{strtime}")
     elif "your name" or "name " in query:
         #strtime = datetime.datetime.now().strftime("%H hours %M minutes%S seconds")
         speak("Am Chitti !Manufacturing Date 30 october 2019!Speed you Cant Think ")


     elif "flag "in query:
         speak("Thankyou for using Me!have a nice day")
         flag=0
     else:
         speak("No Answers")



#while != true:

