import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and synthesis engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Please say something:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print("Error; {0}".format(e))
            return ""

# Function to synthesize speech
def synthesize_speech(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    text = recognize_speech()
    if text:
        synthesize_speech("You said: " + text)