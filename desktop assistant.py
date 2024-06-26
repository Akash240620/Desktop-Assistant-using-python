import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good morning Akash!")
            speak("Good morning Akash!")
        elif hour>=12 and hour<18:
            print("Good afternoon Akash!!")
            speak("Good afternoon Akash!!")
        else:
            print("Good evening Akash!!")
            speak("Good evening Akash!!")
        print("Hello, I am Luna. Please tell me how may i help you?")
        speak("Hello, I am Luna. Please tell me how may i help you?")

def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)   
            r.energy_threshold = 6000  
            r.pause_threshold=1
            audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again, please...")
            return "None"
        return query

def select_song(music_dir):
    print("Would you like to select a specific song or should I play a random one?")
    speak("Would you like to select a specific song or should I play a random one?")
    choice = takeCommand().lower()
    print("User choice:", choice)   
    if 'select ' in choice:
        songs = os.listdir(music_dir)
        print("Here are your options:")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song}")
        print("Please tell me the name of the song you'd like to play.")
        speak("Please tell me the name of the song you'd like to play.")
        song_name = takeCommand().lower()
        print("User song name:", song_name)  
        matching_songs = [s for s in songs if song_name in s.lower()]
        if matching_songs:
            return os.path.join(music_dir, matching_songs[0])
        else:
            print("Sorry, I couldn't find the song. Playing a random one.")
            speak("Sorry, I couldn't find the song. Playing a random one.")
            return os.path.join(music_dir, random.choice(songs))
    elif 'random' in choice:
        return os.path.join(music_dir, random.choice(os.listdir(music_dir)))
    elif 'stop' in choice and 'music' in choice:
        return "stop"  
    else:
        print("Invalid choice. Playing a random song.")
        speak("Invalid choice. Playing a random song.")
        return os.path.join(music_dir, random.choice(os.listdir(music_dir)))

    
if _name=="main_":
    wishMe()
    listening = True
    while listening:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)
                exit()

            elif 'open youtube' in query:
                print("Sure, opening youtube")
                speak("Sure, opening youtube")
                webbrowser.open("youtube.com")
        
            elif 'open google' in query:
                print("Sure, opening Google")
                speak("Sure, opening Google")
                webbrowser.open("google.com")
            
            elif 'music' in query or 'songs' in query or 'song' in query:
                music_dir = 'C:\\Users\\akash\\Desktop\\projects\\songs'
                selected_song = select_song(music_dir)
                os.startfile(os.path.join(music_dir, selected_song))

            elif 'increase volume' in query:
                current_volume = engine.getProperty('volume')
                new_volume = min(1.0, current_volume + 0.1)  
                engine.setProperty('volume', new_volume)
                speak(f"Volume increased to {new_volume:0%}")

            elif 'decrease volume' in query:
                current_volume = engine.getProperty('volume')
                new_volume = max(0.0, current_volume - 0.1)  
                engine.setProperty('volume', new_volume)
                speak(f"Volume decreased to {new_volume:0%}")

            elif 'stop music' in query:
                os.system("")  
            
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")

            elif 'how r u' in query or 'how are you' in query:
                print("I am good! what about you ?")
                speak("I am good! what about you ?")

            elif 'i am also good' in query or 'i am good' in query or 'i m good' in query or 'i m also good' in query:
                print("Great! good to hear that.")
                speak("Great! good to hear that.")
                
            elif 'stop luna' in query or 'quit luna' in query or 'exit luna' in query:
                print("Goodbye AKASH, Have a lovely day!")
                speak("Goodbye AKASH, Have a lovely day!")
                listening = False