import pyttsx3 
import speech_recognition as sr 
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif time>=12 and time<18:
        print("Good Afternoon!")  
        speak("Good Afternoon!")   
    else:
        print("Good Evening!")
        speak("Good Evening!")  
    print("I am your A.I.") 
    speak("I am your A.I.")
    print("I can perform some specific tasks for you") 
    speak("I can perform some specific tasks for you")
    print("How may i help you today") 
    speak("How may i help you today")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query          
 

#wishme()


while True:
    
    query = takecommand().lower()
    if 'what is the time' in query:
        time =(datetime.datetime.now().strftime("%H:%M"))
        print(time)
        speak("the current time is")
        speak(time)
    
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe %s").open("http://www.youtube.com/")

    elif 'open google' in query:
        chrome="C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(chrome)

    elif 'domain expansion' in query:
        os.startfile("C:\\Users\\abhay\\AppData\\Local\Programs\\Lively Wallpaper\\Lively.exe")
        time.sleep(6)
        os.startfile("C:\Program Files\Rainmeter\Rainmeter.exe")
    
    elif 'close domain' in query:
        os.system('taskkill/im Lively.exe /f')
        os.system('taskkill/im Rainmeter.exe /f')

    elif 'open itunes' in query:
        itunes = "C:\Program Files\WindowsApps\AppleInc.iTunes_12130.9.2003.0_x64__nzyj5cx40ttqa\iTunes.exe"
        os.startfile(itunes)


'''
develop in future for 
- playing music
- ask username
- how sre you
- tell time
Find my IP address
Search on Wikipedia
Play videos on YouTube
Search on Google
Send WhatsApp message
Send Email
Get Latest News Headlines
Get Weather Report
Get Trending Movies
Get Random Jokes
Get Random Advice
add if block in opening stuff
'''