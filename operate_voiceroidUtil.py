import pyperclip
import pyautogui
import os
import re
import sys
import time
import subprocess

# coding: UTF-8


def checkPlay():
        try:
                pos = pyautogui.locateCenterOnScreen('play.PNG', region=(0,0, 1000, 1000))
                print("found")
                return False
        except TypeError:
                print("Type Error")
                return True


print('defaultencoding:', sys.getdefaultencoding())

files = os.listdir("./output")
count = 0
for file in files:
        index = re.search(".txt", file)
        if index:
                count = count + 1
print("変換ファイル数: "+str(count))

word_list = []
origin = 0
for i in range(count):
        path = "./output/voice_" + str(i+origin) + ".txt"
        with open(path,'r',encoding="utf-8") as f:
                s = f.read()
                print(s)
                word_list.append(s)
print()

for j in range(count):
        print(j)
        print(word_list[j])
        flg = True
        print("play検索")
        while flg:
                flg = checkPlay()

        pyautogui.click(500, 500)
        pyperclip.copy(word_list[j])
        pyautogui.hotkey('ctrl','v')

        time.sleep(0.1)

        pyautogui.hotkey('f6')
        print("保存待機中...")
        time.sleep(2.5)
        if (j%100)==0 and j!=0:
                cmd = 'taskkill /im VoiceroidEditor.exe'
                returncode = subprocess.call(cmd)
                time.sleep(1)
                pyautogui.typewrite("tab")
                time.sleep(1)
                pyautogui.typewrite("enter")
                time.sleep(3)
                subprocess.Popen("C:\Program Files (x86)\AHS\VOICEROID2\VoiceroidEditor.exe")
                time.sleep(5)