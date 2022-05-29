import ctypes

path = 'E:\\питон2\\Эмин\\обои\\01.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)