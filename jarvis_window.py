from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser as wb
import os

def window():
    root=Tk()
    root.title('Time Bar')

    def time_show():
        current_time=datetime.now()
        new_time=current_time.strftime('%H : %M : %S \n %D')
        lb.config(text=new_time,font=('ariel 30 bold '),bg='black',fg='white')
        root.after(1000,time_show)
        

    lb=Label(root,text='')
    lb.pack()
    
    root.after(1000,time_show)
    time_show()
        

   

    root.mainloop()



sp=pyttsx3.init()
def speak(text):
    sp.say(text)
    sp.runAndWait()

def camera():
     pass

def listen_commmand():
    r=sr.Recognizer()
    with sr.Microphone() as sorce:
        print("Listinig command.......")
        r.adjust_for_ambient_noise(sorce)
        audio=r.listen(sorce)
        try:
            commad=r.recognize_google(audio)
            print(f'you said : {commad}')
            
            return commad.lower()
        except sr.UnknownValueError:
            speak("something went wrong")   


        except sr.RequestError:
            speak("sorry the server is not responding")

def take_comomand(command):
    if 'time' in command:
        speak('opening time and current date sir')
        window()

    elif 'youtube' in command:
        speak("opening youtube")
        wb.open("https://www.youtube.com")
    
    elif "facebook" in command:

        
        speak("Opening Facebook")
        wb.open("https://www.facebook.com")

    elif "google" in command:
        speak("Opening Google")
        wb.open("https://www.google.com")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "exit" in command or "close" in command:
        speak("Goodbye!")
        exit()
    elif 'camera' in command:
        camera()


speak('jarvis activated \n waiting for the command ')
while True:
    user_command=listen_commmand()
    if user_command:
        take_comomand(user_command)