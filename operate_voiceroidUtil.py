import pyautogui
import os
import re
import sys
import time

util_x = 500
util_y = 500

pyautogui.click(util_x, util_y)
pyautogui.typewrite("Hello World")
pyautogui.hotkey('ctrl','s')

files = os.listdir("./output")
count = 0
for file in files:
    index = re.search(".txt", file)
    if index:
        count = count + 1
i = 0
for i in range(count):
        path = "./output/voice_" + str(i) + ".txt"
        file_data = open(path, "r")
        for line in file_data:
                pyautogui.click(util_x, util_y)
                pyautogui.typewrite(line)
                pyautogui.hotkey('ctrl','s')
                print(line)
                time.sleep(2)
 
        file_data.close()
        
