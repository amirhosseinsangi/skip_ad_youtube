import pyautogui
import time
import os

image_path = r" your image path "

print("Skip Ad")

while True:
    try:
        
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)

        if location:
            print(f"path: {location}")

            
            pyautogui.moveTo(location, duration=0.3)

            
            pyautogui.click()
            print("click")

            time.sleep(3)
        else:
            print("not fund")

    except Exception as e:
        print(f"check {e}")

    time.sleep(1)
