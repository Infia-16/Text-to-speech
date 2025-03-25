import pyttsx3
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')
def preprocess_text(text):
    sentences=sent_tokenize(text)
    stop_words=set(stopwords.words('english'))
    processed_sentences=[]
    for sentence in sentences:
        words=word_tokenize(sentence)
        filtered_words=[word for word in words if word.lower() not in stop_words]
        processed_sentences.append(''.join(filtered_words))
    return processed_sentences
def text_to_speech(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    sentences = preprocess_text(text)
    for sentence in sentences:
        print(f"Speaking: {sentence}")
        engine.say(sentence)
        engine.runAndWait()
text = "Hello!"
text_to_speech(text)
def text_to_speech(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    sentences = preprocess_text(text)
    for sentence in sentences:
        print(f"Speaking: {sentence}")
        engine.say(sentence)
        engine.runAndWait()
text = "Hello!"
text_to_speech(text)
def text_to_speech(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    sentences = preprocess_text(text)
    for sentence in sentences:
        print(f"Speaking: {sentence}")
        engine.say(sentence)
        engine.runAndWait()
text = "Howareyou?"
text_to_speech(text)
def text_to_speech(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    sentences = preprocess_text(text)
    for sentence in sentences:
        print(f"Speaking: {sentence}")
        engine.say(sentence)
        engine.runAndWait()
text = "Iamfine!"
text_to_speech(text)