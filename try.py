import time
import pyautogui

ID = ["hanjungwoo1", "hanjungwoo2"]
password = ["1234", "1235"]



for x,y in zip(ID,password):
    print(x, y)






while True:
    time.sleep(2)
    print(pyautogui.position())


