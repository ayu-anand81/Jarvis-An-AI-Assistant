import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https:/google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https:/instagram.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https:/instagram.com")
    elif "open youtube" or "open yt" in c.lower():
        webbrowser.open("https:/youtube.com")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Intailizing Jarvis....")
    while True:
        #Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout= 5 , phrase_time_limit= 5)

            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Yes Sir")
                print("Listening for command...")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error {0}".format(e))