import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

def process_command(command):
    if "hello" in command:
        return "Hello! How can I help you Piyush Sir?"
    elif "hello" in command:
        return "It's my pleasure to help you out sir"
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Google is now open."
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        return "YouTube is now open."
    elif "song" in command:
        webbrowser.open("https://open.spotify.com/playlist/2EzEPsSm88abWRuhNZ9Wv0/")
        return "Your playlist is now open."
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return f"Searching for {search_query}..."
    elif any(w in command for w in ['who', 'whose','whom','where','which','when','why','what']):
        try:
            search_query = command.split(' ', 1)[1]
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            return f"Searching on Google for {search_query}..."
        except Exception as e:
            return "Sorry, I couldn't process your request at the moment."
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple results found. Please be more specific."
        except wikipedia.exceptions.PageError as e:
            return f"Sorry, no information found for {query}."
        except Exception as e:
            return "Sorry, I couldn't retrieve information from Wikipedia at the moment."
    elif any(op in command for op in ['+', '-', '*', '/']):
        try:
            result = eval(command)
            return f"The result is {result}"
        except Exception as e:
            return "Sorry, I couldn't compute that."
    elif "exit" in command or "stop" in command:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

def speak(response):
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I'm your Jarvis. Piyush sir. How can I help you today?")
    while True:
        user_input = listen()

        if user_input:
            response = process_command(user_input)
            speak(response)

            if "exit" in user_input or "stop" in user_input:
                break
