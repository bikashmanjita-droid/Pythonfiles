
import pywhatkit as kit
from datetime import datetime
import pyautogui
import time

phone_number = '+9779707860140'  # Example: +14155552671


message = 'maile msg gareko xaina k practice gariraxu ma '

now = datetime.now()
send_hour = now.hour
send_minute = now.minute + 1


kit.sendwhatmsg(phone_number, message, send_hour, send_minute)


pyautogui.press('enter')

