import pyautogui
import os
import re

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
                print(line)
 
# 開いたファイルを閉じる
        file_data.close()
        
