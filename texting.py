import pyautogui
import time
import random
from config import *

def write():
    try:
        discord_window = pyautogui.getWindowsWithTitle("Discord")[0]
        discord_window.activate()
        time.sleep(0.1)
        discord_window.maximize()
        
        chat = pyautogui.locateOnScreen("write.png", confidence=Settings.confidence)
        if chat is None:
            print("Chat box not found on the screen.")
            return
        
        for image in Settings.images:
            location = pyautogui.locateOnScreen(image, confidence=Settings.confidence)
            if location is not None:
                pyautogui.click(location)
                pyautogui.click(chat)
                text = random.choice(Settings.texts) 
                pyautogui.write(text, 0.02)
                pyautogui.press("enter")
                break
        
        else:
            print("No image was found on the screen with sufficient confidence.")
    
    except IndexError:
        print("Discord window not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    time.sleep(60)
while True:
    if __name__ == "__main__":
        write()
