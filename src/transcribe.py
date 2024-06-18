import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)
    with audio_file as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    return None

if __name__ == "__main__":
    transcription = transcribe_audio('emergency.wav')
    if transcription:
        print("Transcription:", transcription)
