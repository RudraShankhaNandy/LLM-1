from google.cloud import speech_v1p1beta1 as speech
import io

import speech_recognition as sr
import keyboard

def listen_continuous():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")

        # Check for an interruption signal (e.g., pressing 'q' to quit)
        if keyboard.is_pressed("q"):
            print("Continuous listening stopped.")
            break
        return text

# Start continuous listening
listen_continuous()

