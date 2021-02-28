import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
from datetime import datetime
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    playsound('./sound/alert.mp3')
    audio = r.record(source, duration=5)
    playsound('./sound/alert.mp3')

    try:
        text = r.recognize_google(audio, language='th')
        if("spotify" in text):
            text = text.replace(text, "ได้เลยค่ะ")
            os.system('Start Spotify')
        if('Google' in text):
            text = text.replace(text, "กำลังเปิด Google")
            os.system('Start chrome')
    except:
        text = "ขอโทษค่ะฉันไม่เข้าใจที่คุณพูด"
    tts = gTTS(text, lang='th')
    print(text)
    tts.save('./answer.mp3')
    playsound('./answer.mp3')