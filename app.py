from flask import Flask, request, jsonify
import speech_recognition as sr

app=Flask(__name__)


def audio(audiofile):
    # object creation
    recogniser=sr.Recognizer()
    with sr.AudioFile(audiofile) as source:
        #listens the audio file
        audio_data=recogniser.record(source)
        text=recogniser.recognize_google(audio_data) #converts into text
        text=text.lower()
        return text


@app.route('/')
def home():
    return "Hello! Speech Recognition Route"

@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    if 'file' not in request.files:
        return jsonify({"message":"No file part"}) 

    file=request.files['file']
    if file.filename=='':
        return jsonify({"message":"No file part"}) 

    try:
        text=audio(file)
        return jsonify({"message" : text})
    except sr.UnknownValueError:
        return jsonify({"message": "Could not understand audio"})
    except sr.RequestError as e:
        return jsonify({"message": f"Error fetching results: {e}"})

if __name__=="__main__":
    app.run(debug=True)

