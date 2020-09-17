import pyautogui
import time
import timeit
time.sleep(2)
pyautogui.moveTo(1770,264)
print("Starting Search")
while True:
    x,y = pyautogui.position()
    start_time = timeit.default_timer()
    loc = pyautogui.locateCenterOnScreen('button.png',confidence=0.7, region = (353,80,1217,765))
    if loc != None:
        print("Found Accept Button")
        print(f"Clicking {loc}")
        pyautogui.click(loc)
        pyautogui.moveTo(x,y)
    loadingin = pyautogui.locateCenterOnScreen('loading.png',confidence=0.6, region = (353,80,1217,765))
    if loadingin != None:
        print("Loading into match")
        print("Stopping program")
        break
    #print(timeit.default_timer()-start_time)
    time.sleep(1.5)
