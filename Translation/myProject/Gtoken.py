import speech_recognition as sr
from googletrans import Translator

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak in Telugu...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='te-IN')
        print("You said (Telugu):", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return None

# Function to translate text
def translate_text(text, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    print("Translated (English):", translation.text)
    return translation.text

# Main function
def main():
    # Recognize speech in Telugu
    telugu_text = recognize_speech()
    
    # If speech was recognized, translate to English
    if telugu_text:
        english_text = translate_text(telugu_text)
        # Do whatever you want with the translated text, like saving it to a file
        with open("translated_text.txt", "w", encoding="utf-8") as file:
            file.write(english_text)
        print("Translated text saved to 'translated_text.txt'.")

if __name__ == "__main__":
    main()
