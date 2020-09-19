import pyautogui
import time
import timeit
import pathlib
import logging
logging.basicConfig(format='Time to search for images = %(message)s',level=logging.DEBUG)
logging.disable()
parent = pathlib.Path(__file__).resolve().parent
mypath = pathlib.Path(parent)
buttonpath = mypath / 'button.png'
button2path = mypath / 'button2.png'
loadingpath = mypath / 'loading.png'
art = """
   ___ ___  ___  ___      _       _         _                  _
  / __/ __|/ __|/ _ \    /_\ _  _| |_ ___  /_\  __ __ ___ _ __| |_ ___ _ _
 | (__\__ \ (_ | (_) |  / _ \ || |  _/ _ \/ _ \/ _/ _/ -_) '_ \  _/ -_) '_|
  \___|___/\___|\___/  /_/ \_\_,_|\__\___/_/ \_\__\__\___| .__/\__\___|_|
                                                         |_|
                                                         """
print(art)
print("Starting Search")
while True:
    x,y = pyautogui.position()
    start_time = timeit.default_timer()
    loc = pyautogui.locateCenterOnScreen(str(buttonpath), grayscale = True)
    loc2 = pyautogui.locateCenterOnScreen(str(button2path), grayscale = True)
    if loc:
        print("Found Accept Button")
        print(f"Clicking {loc}")
        pyautogui.click(loc)
        pyautogui.moveTo(x,y)
        time.sleep(2)
    elif loc2:
        print("Found Moused Over Accept Button")
        print(f"Clicking {loc2}")
        pyautogui.click(loc2)
        pyautogui.moveTo(x,y)
        time.sleep(2)
    loadingin = pyautogui.locateCenterOnScreen(str(loadingpath), grayscale = True)
    if loadingin != None:
        print("Loading into match")
        print("Stopping program")
        break
    logging.debug(timeit.default_timer()-start_time)
