print("Whatsapp Bot Messaging Programme By Somu!")
import pyautogui
import time
time.sleep(5)
count=1
n=int(input("Enter the number of message: "))
while count<=n:
    pyautogui.sleep(1)
    pyautogui.typewrite("Hey! Bro ")
    # if u want to add count - -  thrn add in write ------   +str(count)
    pyautogui.press("Enter")
    pyautogui.sleep(1)
    count=count+1