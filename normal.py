import speech_recognition as sr
import pyttsx3
import webbrowser
import os

a = pyttsx3.init('sapi5')
voices = a.getProperty('voices')
a.setProperty('voice', voices[1].id)

def speak(audio):
    a.say(audio)
    a.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("You may give your command")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Command is: {query}\n")
    except Exception as e:
        speak("Please try to give another command")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("You may start watching videos on YouTube")
        elif 'run my react app' in query:
            project_directory = r"E:\2024Uni\WebProg\bmicalculator"
            os.chdir(project_directory)
            os.system('npm start')
            speak("React app is running")
