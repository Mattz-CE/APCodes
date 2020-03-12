#pip installs PyAudio, pythoncom
#system('say Hello world!')
from os import system
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        system('Good Morning!')

    elif hour>=12 and hour<18:
        system("Good Afternoon!")   

    else:
        system("Good Evening!")  

    system("Hey!")        

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            system('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            system("According to Wikipedia")
            print(results)
            system(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            system(f"Sir, the time is {strTime}")

        elif 'email to harry' in query:
            try:
                system("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                system("Email has been sent!")
            except Exception as e:
                print(e)
                system("Sorry my friend harry bhai. I am not able to send this email")    
