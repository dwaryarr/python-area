import pyautogui,time
time.sleep(5)

with open("text.txt","r") as t:
    for word in t:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
time.sleep(5)