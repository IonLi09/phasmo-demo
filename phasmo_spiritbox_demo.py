import pyttsx3
import speech_recognition
import random

# data

age_keywords = ['old', 'young', 'child', 'born', 'adult']
location_keywords = ['here', 'close', 'show', 'yourself', 'us', 'room', 'where']
general_keywords = ['sign', 'angry', 'talk', 'speak', 'want', 'leave', 'wrong', 'friendly', 'color']

age_responses = ['old', 'young', 'adult', 'child']
location_responses = ['i\'m here', 'behind you', 'next', 'away', 'far', 'close']
general_responses = ['kill', 'die', 'death', 'hate', 'attack', 'hurt']

keywords = {
    'age' : age_responses,
    'location' : location_responses,
    'general' : general_responses
}

print('ctrl-c to exit')

# speech recognizer

while True:
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Say Something: ')
        audio = recognizer.listen(source)

    words = recognizer.recognize_google(audio)

    found = False

    for cat in keywords:
        if cat == 'age':
            searchCat = age_keywords
        elif cat == 'location':
            searchCat = location_keywords
        else:
            searchCat = general_keywords
        for word in searchCat:
            if word in words:
                response = random.choice(keywords[cat])
                found = True
                break
        if found:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(response)
            engine.runAndWait()
            # pyttsx3.speak(response)
            break