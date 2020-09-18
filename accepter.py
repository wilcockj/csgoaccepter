import pyautogui
import time
import timeit
import pathlib
parent = pathlib.Path(__file__).resolve().parent
mypath = pathlib.Path(parent)
buttonpath = mypath / 'button.png'
loadingpath = mypath / 'loading.png'
print("Starting Search")
while True:
    x,y = pyautogui.position()
    start_time = timeit.default_timer()
    loc = pyautogui.locateCenterOnScreen(str(buttonpath),confidence=0.7)
    if loc != None:
        print("Found Accept Button")
        print(f"Clicking {loc}")
        pyautogui.click(loc)
        pyautogui.moveTo(x,y)
    loadingin = pyautogui.locateCenterOnScreen(str(loadingpath),confidence=0.6)
    if loadingin != None:
        print("Loading into match")
        print("Stopping program")
        break
    time.sleep(1.5)
