import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import webbrowser as wb
import sys 
import itertools
import os
import ctypes
import colorama
from colorama import Fore
import pyautogui

colorama.init()

def text():
    it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
    for x in range(2):
        time.sleep(.3)  # выполнение функции
        print(next(it), end='', flush=True)
    print('\nDone.')

def talk(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait() 

text()

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk('слушаю вас')
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

    elif 'с новым годом' in task:
        nyp_f = nyp()
        talk('с новым 2022-ым годом')
        print('с новым 2022 годом!')
    
    elif 'новый год закончился' in task:
        anyp_f = anyp()
        talk('надеюсь вы повеселились')
        print('надеюсь вы повеселились')
    
    elif 'создай новый тестовый файл' in task:
        import auto_file_creation
    
    elif 'открой vk' in task:
        talk ('открываю вк мьюзик')
        wb.open('https://vk.com/audios582614583?section=all')
        time.sleep(8)
        pyautogui.hotkey('altleft', 'k')
    
    elif 'открой браузер' in task:
        talk('открываю браузер')
        wb.open('Opera') 

    elif 'что такое' in task:
        request = task.replace('что такое ', '')
        talk ('вот что я нашла по запросу{0}'.format(request))
        print('вот что я нашла по запросу{0}'.format(request))
        wb.open('https://www.google.by/search?q={0}&source=hp&ei=za3IYZWkB4r0U7esktAO&iflsig=ALs-wAMAAAAAYci73Y6jwM7h_ylx6AS4RpTLRPNRjXdX&ved=0ahUKEwjVvvzvhYL1AhUK-hQKHTeWBOoQ4dUDCAY&uact=5&oq=food&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDILCC4QgAQQxwEQrwEyCwguEIAEEMcBEK8BMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BMgUIABCABDILCC4QgAQQxwEQrwEyBQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6CAguELEDEIMBOgUILhCABDoICC4QgAQQsQM6CwguEIAEEMcBENEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQowJQAFilBGCwBWgAcAB4AIABaogB6AKSAQMzLjGYAQCgAQE&sclient=gws-wiz'.format(request))

    elif 'что ты умеешь' in task:
        talk ('на данный момент у вас 8 команд')
        talk ('я вывела их в командную строку')
        print ('''
        1 - проверка (команда для проверки исправности модулей)
        2 - с новым годом (команда запускает новогодний модуль)
        3 - новый год закончился (команда дизактивирует новогодний модуль)
        4 - создай новый тестовый файл (создаёт пайтон файл и вписывает стандартную команду для проверки)
        5 - открой вк (открывает вк)
        6 - открой браузер (открывает браузер)
        7 - что такое ... (команда чтобы искать что либо в гугле)
        8 - что ты умеешь (показывает список команд)
        9 - стоп (закрывает голосового  помошника сара)
        ''')
        talk('последуйщие команды будут приняты через 15 секунд')
        time.sleep(15)

    elif 'стоп' in task:
        talk ('ещё услышимся')
        sys.exit()

while True:
    mst(task = command())