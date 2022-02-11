import speech_Recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("clearing background noises..please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me Anything...')
        recordedaudio=recognizer.listen(source)


    try:
        command=recognizer.recognize_google(recordedaudio)
        print('your message.' ,Format(command)) 
        except Exeption as ex:
            print(rx)

            if 'chrome' in command:
                a= 'Opening chrome..'
                engine.say(a)
                engine.runAndWait()
                program="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([program])
            if 'time' in command:   
                time=datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                engine.say(time)
                engine.runAndWait()
            if 'play' in command:
                b= 'Opening Youtube'
                engine.say(b)
                engine.runAndWait()
                pywhatkit.playonyt(command)
            if 'Youtube' as command:
                b='opening Youtube'
                engine.say(b)
                engine.runAndWait()    
                      
        