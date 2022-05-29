import win32gui

toplist = []
winlist = []
def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

win32gui.EnumWindows(enum_callback, toplist)
opera = [(hwnd, title) for hwnd, title in winlist if 'opera' in title.lower()]
# just grab the first window that matches
opera = opera[0]
# use the window handle to set focus
win32gui.SetForegroundWindow(opera[0])