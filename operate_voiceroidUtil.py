import pyperclip
import pyautogui
import os
import re
import sys
import time
# coding: UTF-8
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
        with open(path,'r') as f:
                s = f.read()
                print(s)
                word_list.append(s)
print()


img_play_x,img_play_y = pyautogui.locateCenterOnScreen('play.PNG',grayscale=True,region=(0,0, 1000, 1000))

for j in range(count):
        print(j)
        flg = True
        print("保存待機中...")
        while flg:
                if pyautogui.onScreen(img_play_x, img_play_y):
                        flg = False
                else:
                        flg = True
        time.sleep(0.5)
        img_x,img_y = pyautogui.locateCenterOnScreen('inputArea.PNG',grayscale=True,region=(0,0, 1000, 1000))
        pyautogui.moveTo(img_x+100, img_y+100, duration=0.1)
        pyautogui.click(img_x+100, img_y+100)
        #pyautogui.click(util_x, util_y)
        pyperclip.copy(word_list[j])
        pyautogui.hotkey('ctrl','v')
        time.sleep(0.2)
        pyautogui.hotkey('f6')
        print(word_list[j])
        time.sleep(0.5)
