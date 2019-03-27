import pyautogui
import os
import re

files = os.listdir("./output")
count = 0
for file in files:
    index = re.search(".txt", file)
    if index:
        count = count + 1

for i in range(count):
    path = "./output/voice_" + str(i)
    with open(path, mode='r') as f:
        text = f.readLine()
        
