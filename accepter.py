import pyautogui
import time
import timeit
import pathlib
parent = pathlib.Path(__file__).resolve().parent
mypath = pathlib.Path(parent)
buttonpath = mypath / 'button.png'
loadingpath = mypath / 'loading.png'
button2path = mypath / 'button2.png'
print("Starting Search")
while True:
    x,y = pyautogui.position()
    start_time = timeit.default_timer()
    loc = pyautogui.locateCenterOnScreen(str(buttonpath),confidence=0.7)
    loc2 = pyautogui.locateCenterOnScreen(str(button2path),confidence=0.7)
    if loc:
        print("Found Accept Button")
        print(f"Clicking {loc}")
        pyautogui.click(loc)
        pyautogui.moveTo(x,y)
    elif loc2:
        print("Found Moused Over Accept Button")
        print(f"Clicking {loc2}")
        pyautogui.click(loc2)
        pyautogui.moveTo(x,y)
    loadingin = pyautogui.locateCenterOnScreen(str(loadingpath),confidence=0.6)
    if loadingin != None:
        print("Loading into match")
        print("Stopping program")
        break
    time.sleep(0.5)
