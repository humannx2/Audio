import speech_recognition as sr
import pyttsx3
object=sr.Recognizer() #object creation
listening=False
while True:
    try:
        with sr.Microphone() as mic:
            # controls the duration of mic recording
            object.adjust_for_ambient_noise(mic,duration=0.2)
            if not listening:
                print("Say 'Start' to begin the Recognition and 'Stop' to end.")
                audio=object.listen(mic)
                start_stop=object.recognize_google(audio)
                start_stop=start_stop.lower()
                if "start" in start_stop:
                    listening=True
                    print("Listening! Say Something")
                continue
            audio=object.listen(mic)
            # using google library to convert audio into text
            text=object.recognize_google(audio)
            text=text.lower()
            if "stop" in text:
                listening = False
                print("Listening Stopped!")
                exit()
            else:
                print(f"Recognized Text is: {text}")
    except sr.UnknownValueError:
        continue