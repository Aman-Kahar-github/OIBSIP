import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=10)

        print("Recognizing...")

        # Recognize speech using Google Speech Recognition
        query = recognizer.recognize_google(audio)

        print("You said:", query)

        # Process commands
        if "hello" in query.lower():
            speak("Hello! How can I help you?")
        elif "what is your name" in query.lower():
            speak("My name is GEKKO ")
        elif "how are you" in query.lower():
            speak("I'm doing well, thank you!")
        elif "time" in query.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("It's " + current_time)
        elif "date" in query.lower():
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today's date is " + current_date)
        elif 'open google' in query.lower():
            webbrowser.open("google.com")
        elif 'open instagram' in query.lower():
            webbrowser.open("instagram.com")
        elif 'weather' in query.lower():
            webbrowser.open("accuweather.com")
        elif 'open calculator' in query.lower():
            webbrowser.open("calculator.net")
        elif "play music" in query.lower():
            speak("opening spotify.")
            webbrowser.open("open.spotify.com")
        elif "tell a joke" in query.lower():
            speak("Why couldn't the bicycle find its way home? It lost its bearings!")
        elif "stop" in query.lower():
            speak("Stopping...")
        elif "thank you" in query.lower():
            speak("You're welcome!")
        elif "goodbye"or"good bye" in query.lower():
            speak("Goodbye!")
            break  # Exit the loop
        else:
            speak("Sorry, I didn't understand that.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
