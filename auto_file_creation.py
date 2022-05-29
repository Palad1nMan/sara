import pyautogui 
import time
def place():
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
place()
