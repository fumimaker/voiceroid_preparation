import re
#!/usr/bin/python
# coding: UTF-8
with open("./counter.txt", mode='r') as f:
    fileCounter = int(f.read())

f = open('./input.txt',encoding="utf-8")
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
for line in lines1:
    print(line)
    tex_list = re.split('。|、|！|？', line)
    print(tex_list)
    for i in tex_list:
        if (i != '' ) or (i != ' '):
            path_w = "./output/voice_" + str(fileCounter) + ".txt"
            with open(path_w, mode='w',encoding="utf-8") as f:
                f.write(str(i))
                fileCounter = fileCounter + 1
                
with open("./counter.txt", mode='w') as f:
    f.write(str(fileCounter))
