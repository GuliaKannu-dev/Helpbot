# Author: Krmbir
# Topic: Chatbot

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Get the available voices and set the voice property
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set to the first voice

def speak(audio):
    """Function to convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to wish the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your intelligent service bot. How can I help you?")

def takecommand():
    """Function to take voice command from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User  said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query

def play_music():
    """Function to play a random song from the music directory."""
    music_dir = 'F:\\New punjabi songs'  # Ensure this path is correct
    songs = os.listdir(music_dir)
    if songs:
        song = random.choice(songs)  # Select a random song
        os.startfile(os.path.join(music_dir, song))
        speak(f"Playing {song}")
    else:
        speak("No songs found in the music directory.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        # Logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            play_music()  # Call the new function

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Karambir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")  # Open WhatsApp Web

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")  # Open Facebook

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")  # Open Twitter

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")  # Open Instagram

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day!")
            break  # Exit the loop

        