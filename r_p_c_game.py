import pyttsx3 
import speech_recognition as sr
import random


game_options = ['rock', 'paper', 'scissors']
sp = pyttsx3.init()

def speak(txt):
    sp.say(txt)
    sp.runAndWait()

def listen_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("please give me your choice")
        speak("please give me your choice")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.RequestError:
        speak('The server is not responding.')
    except sr.UnknownValueError:
        speak("I didn't catch that. Please try again.")
    return None

def response_user(user_choice):
    word='offline'
    com_choice = random.choice(game_options)
    if word in user_choice:
        from rock_paper_seasor import r_p_c_game

        print('inititiling without virtual voice game')
        speak('inititiling without virtual voice game')
        print("Press 'q' to quit.")

        

        
    

        r_p_c_game()
        
    

    elif user_choice == com_choice:
        print(f'i chose {com_choice} \n\
               you chose {user_choice} \
                game draw')
      
        speak(f'i chose {com_choice} \n\
               you chose {user_choice} \
                game draw')

    
        
    elif user_choice not in game_options:
        speak(f'{user_choice} is not a valid option.')
    elif (user_choice == 'rock' and com_choice == 'scissors') or \
         (user_choice == 'paper' and com_choice == 'rock') or \
         (user_choice == 'scissors' and com_choice == 'paper'):
             
             speak(f'i chose {com_choice} \n you chose {user_choice} \n you win')
    elif 'type' in user_choice:
        from rock_paper_seasor import r_p_c_game

        r_p_c_game()
        

        
        
             
    else:
        
        print(f'i chose{com_choice} you chose {user_choice} You lose!')
        speak(f'i chose{com_choice} you chose {user_choice} You lose!')



while True:
    user = listen_user()
    if user:
        if 'quit' in user or 'exit' in user:
            speak('Thanks for playing. Goodbye!')
            break
        else:
            response_user(user)
