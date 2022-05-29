import time
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
from pyowm import OWM
import math
import random
import wikipedia

colorama.init()

def talk(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait() 


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(Fore.WHITE + 'готов к работе')
        talk ('готов к работе')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
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

def WeatherForToDay():
    #---------settings---------#
    owm = OWM('25c2b543381b027be11917003d8f93df')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Minsk,BY')
    w = observation.weather
    temp = w.temperature('celsius')

    #-----------main-----------#
    ti = temp['temp']
    min = math.ceil(ti)
    max = math.floor(ti)
    talk('{0} тере {1}° по цельсию'.format(min, max))
 
def password():
    passnum = random.randrange(0, 100000000) 
    keyword = 'P_aSSword'
    passwoed = keyword + str(passnum)
    print(Fore.GREEN + passwoed)

def raduga():
    pyautogui.hotkey('alt', 'ctrl', '1')
    pyautogui.hotkey('alt', 'ctrl', '2')
    pyautogui.hotkey('alt', 'ctrl', '3')
    pyautogui.hotkey('alt', 'ctrl', '4')
    pyautogui.hotkey('alt', 'ctrl', '5')
    pyautogui.hotkey('alt', 'ctrl', '1')

def idle():
    os.startfile('E:\питон2\VS CODE\Microsoft VS Code\code')

def filecreate():
    ttx = '''
print ('Hello World')'''
    pyautogui.hotkey('ctrl', 'n')
    pyautogui.moveTo(1800, 1030)
    pyautogui.click()
    pyautogui.typewrite('python')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(0.5)
    pyautogui.typewrite('ptp')
    pyautogui.press('enter')
    pyautogui.typewrite(ttx)
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'f5')

#mst - make some thing
def mst(task):
    if 'проверка' in task or 'проверочка' in task or 'test' in task:
        talk('все системы работают прекрасно')
        print(Fore.YELLOW + 'Done!')

    elif 'с новым годом' in task:
        nyp_f = nyp()
        talk('с новым 2022-ым годом')
        print('с новым 2022 годом!')
    
    elif 'новый год закончился' in task:
        anyp_f = anyp()
        talk('надеюсь вы повеселились')
        print('надеюсь вы повеселились')
    
    elif 'создай новый тестовый файл' in task:
        filecreate()
    
    elif 'включи музыку' in task or 'открой вк мьюзик' in task or 'включи vk мьюзик' in task or 'музыку' in task:
        talk ('открываю вк мьюзик')
        wb.open('https://vk.com/audios582614583?section=all')
        time.sleep(8)
        for i in range(3):
            pyautogui.hotkey('altleft', 'k')

    elif 'открой браузер' in task or 'открой оперу' in task or 'браузер' in task:
        talk('открываю браузер')
        wb.open('Opera') 

    elif 'найди' in task:
        request = task.replace('найди ', '')
        talk ('вот что я нашла по запросу{0}'.format(request))
        print('вот что я нашла по запросу{0}'.format(request))
        wb.open('https://www.google.by/search?q={0}&source=hp&ei=za3IYZWkB4r0U7esktAO&iflsig=ALs-wAMAAAAAYci73Y6jwM7h_ylx6AS4RpTLRPNRjXdX&ved=0ahUKEwjVvvzvhYL1AhUK-hQKHTeWBOoQ4dUDCAY&uact=5&oq=food&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDILCC4QgAQQxwEQrwEyCwguEIAEEMcBEK8BMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BMgUIABCABDILCC4QgAQQxwEQrwEyBQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6CAguELEDEIMBOgUILhCABDoICC4QgAQQsQM6CwguEIAEEMcBENEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQowJQAFilBGCwBWgAcAB4AIABaogB6AKSAQMzLjGYAQCgAQE&sclient=gws-wiz'.format(request))

    elif 'что такое' in task:
        dop = 'описание слова '
        request = task.replace('что такое ', '')
        talk ('вот что я нашла по запросу{0}'.format(request))
        print('вот что я нашла по запросу{0}'.format(request))
        wb.open('https://www.google.by/search?q={0}{1}ktAO&iflsig=ALs-wAMAAAAAYci73Y6jwM7h_ylx6AS4RpTLRPNRjXdX&ved=0ahUKEwjVvvzvhYL1AhUK-hQKHTeWBOoQ4dUDCAY&uact=5&oq=food&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDILCC4QgAQQxwEQrwEyCwguEIAEEMcBEK8BMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BMgUIABCABDILCC4QgAQQxwEQrwEyBQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6CAguELEDEIMBOgUILhCABDoICC4QgAQQsQM6CwguEIAEEMcBENEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQowJQAFilBGCwBWgAcAB4AIABaogB6AKSAQMzLjGYAQCgAQE&sclient=gws-wiz'.format(dop, request))

    elif 'расскажи погоду на сегодня' in task or 'как там погода за окном' in task or 'прогноз пагоды на сегодня' in task:
        WeatherForToDay()

    elif 'открой idle' in task or 'открой vs code' in task:
        talk('открываю visual studio code')
        idle()
#--------------------громкость/управление звуком--------------------#
    elif 'сделай громче' in task:
        os.startfile('b1\\source\\forsys\\volUp10.lnk')

    elif 'сделай тише' in task:
        os.startfile('b1\\source\\forsys\\volDown10.lnk')

    elif 'выключи звук' in task:
        os.startfile('b1\\source\\forsys\\mute.lnk')

    elif 'ещё громче' in task:
        os.startfile('b1\\source\\forsys\\volUp10.lnk')

    elif 'ещё тише' in task:
        os.startfile('b1\\source\\forsys\\volDown10.lnk')

    elif 'выключи звук' in task:
        os.startfile('b1\\source\\forsys\\mute.lnk')

    elif 'поставь громкость на 100%' in task:
        for i in range(10):
            os.startfile('b1\\source\\forsys\\volUp10.lnk') 

    elif 'громкость на' in task:
        os.startfile('b1\\source\\forsys\\mute.lnk')        
        firststan = task.replace('громкость на ', '')
        secondstan= firststan.replace('0', '')
        for i in range(int(secondstan)):
            os.startfile('b1\\source\\forsys\\volUp10.lnk')
#--------------------громкость/управление звуком--------------------#
    elif 'открой почту' in task or 'открой имейл' in task:
        wb.open('https://mail.google.com/mail/u/0/#inbox')

    elif 'придумай пароль' in task or 'мне нужен пароль':
        password()
        talk('я вывела ваш пароль зелёным цветом в командную строку')   

    elif 'что ты умеешь' in task:
        talk ('на данный момент у вас 22 команд')
        talk ('я вывела их в командную строку')
        print ('''
        1 - проверка (команда для проверки исправности модулей)
        2 - с новым годом (команда запускает новогодний модуль)
        3 - новый год закончился (команда дизактивирует новогодний модуль)
        4 - создай новый тестовый файл (создаёт пайтон файл и вписывает стандартную команду для проверки)
        5 - включи музыку (открывает вк мьюзик)
        6 - сделай радугу (быстро меняет цвет подсветки мыши)
        7 - открой браузер (открывает браузер)
        8 - что такое... (команда чтобы искать описание того что вы сказали)
        9 - найди... (просто ищет слово которое вы сказали)
        10 - открой почту (открывает gmail.com)
        11 - что ты умеешь (показывает список команд)
        12 - раскажи погоду на сеодня (рассказывает погоду на сегодня)
        13 - открой idle (открывает vs code по пути которому вы указали)
        14 - придумай пароль (генерирует пароль)
        15 - сделай громче (делает звук громче)
        16 - сделай тише (делает звук тише)
        17 - выключи звук (выключает звук)
        18 - ещё громче (увеличивает громкость звука на 10)
        19 - ещё тише (уменьшает громкость звука на 10)        
        20 - поставь громкость но 100% ( ставить звук на максимум)
        21 - поставь громкость на 10/20/30/40/50/60/70/80/90% ( ставит звук на 10/20 и т.д. % громкости)
        22 - стоп (закрывает голосового  помошника сара)
        ''')
        talk('последуйщие команды будут приняты через 15 секунд')
        time.sleep(15)

    elif 'стоп' in task:
        talk('ещё услышимся')
        sys.exit()

while True:
    mst(task = command())