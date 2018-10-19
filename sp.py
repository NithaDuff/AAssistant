import speech_recognition as sr
import sys
r = sr.Recognizer();
#filename = sys.argv[1]
with sr.Microphone() as source :
    print("Say something...")
    audio = r.listen(source)
    print("Time over.... :)")
try:
    print("System predicts:"+r.recognize_google(audio))
except Exception :
    pass
    print("Something went wrong")
