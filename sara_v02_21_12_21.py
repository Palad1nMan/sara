import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import webbrowser as wb
import sys 
import os
import ctypes
import colorama
from colorama import Fore
import pyautogui

colorama.init()

def talk(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait() 

talk ('готов к работе')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('готов к работе')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language = "ru-RU").lower()
        print ('[log]: ' +  task)
    except sr.UnknownValueError:
        talk ('ошибка, повторите запрос')
        task = command()
    return task

def nyp():
    wb.open('https://vk.com/audios582614583?section=all&z=audio_playlist582614583_29')

    path = 'E:\\питон2\\Эмин\\ии\\b1\\source\\ny.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

    pyautogui.keyDown('alt')
    pyautogui.keyDown('ctrl')
    pyautogui.press('5')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('ctrl')

def anyp():
    path = 'E:\\питон2\\Эмин\\ии\\b1\\source\\nor.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

    pyautogui.keyDown('alt')
    pyautogui.keyDown('ctrl')
    pyautogui.press('1')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('ctrl')

#mst - make some thing
def mst(task):
    if 'проверка' in task:
        talk('проверка пройдена')
        print(Fore.GREEN,  'Done!')

    elif 'новый год' in task:
        nyp_f = nyp()
        talk('с новым 2022-ым годом')
        print('с новым 2022 годом!')
    
    elif 'нового года не будет' in task:
        anyp_f = anyp()
        talk('надеюсь вы повеселились')
        print('надеюсь вы повеселились')
        
    elif 'стоп' in task:
        talk ('ещё услышимся')
        sys.exit()

while True:
    mst(task = command())