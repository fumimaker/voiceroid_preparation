import pyperclip
import pyautogui
import os
import re
import sys
import time

util_x = 500
util_y = 500

print('defaultencoding:', sys.getdefaultencoding())

files = os.listdir("./output")
count = 0
for file in files:
    index = re.search(".txt", file)
    if index:
        count = count + 1
print(count)

word_list = []

for i in range(count):
        path = "./output/voice_" + str(i) + ".txt"
        with open(path,'r',encoding="utf-8") as f:
                s = f.read()
                print(s)
                word_list.append(s)
print()


for j in range(count):
        print(j)
        pyautogui.click(util_x, util_y)
        pyperclip.copy(word_list[j])
        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('ctrl','s')
        print(word_list[j])
        time.sleep(3)
