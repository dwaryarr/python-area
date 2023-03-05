import pyautogui
import time
time.sleep(3)

text = input("Masukan text : ")
num = int(input("Masukan jumlah spam yang diinginkan: "))
delay = int(input("Masukan delay : "))
time.sleep(3)

for x in range(delay, 0, -1):
    time.sleep(1)
    print("Spam akan dimulai dalam " + str(x) + " detik")
time.sleep(3)

print("Spam dimulai!")

for i in range(int(num)):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    time.sleep(delay)
else:
    print("Spam selesai!")
