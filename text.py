import re
# !/usr/bin/python
# coding: UTF-8
with open("./counter.txt", mode='r') as f:
    fileCounter = int(f.read())
    print("ファイル数は: " + str(fileCounter))

f = open('./input.txt', encoding="utf-8")
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)

l = []
for line in lines1:
    l.append(re.findall(".*?。|.*$", line))

T = []
T = filter(lambda a: a != '', l)
print(T)

"""
    if (i != '') or (i != ' '):
        path_w = "./output/voice_" + str(fileCounter) + ".txt"
        with open(path_w, mode='w',encoding="utf-8") as f:
            f.write(str(i))
            fileCounter = fileCounter + 1
    
with open("./counter.txt", mode='w') as f:
    f.write(str(fileCounter))
"""
