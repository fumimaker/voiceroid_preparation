import re

# !/usr/bin/python
# coding: UTF-8

def flatten_with_any_depth(nested_list):
    """深さ優先探索の要領で入れ子のリストをフラットにする関数"""
    # フラットなリストとフリンジを用意
    flat_list = []
    fringe = [nested_list]

    while len(fringe) > 0:
        node = fringe.pop(0)
        # ノードがリストであれば子要素をフリンジに追加
        # リストでなければそのままフラットリストに追加
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list


def trimingByMark(list, character):
    l = []
    for now_text in list:
        l.append(re.findall(".*?" + character + "|.*$", now_text))

    return flatten_with_any_depth(l)


def main():
    with open("./counter.txt", mode='r') as f:
        fileCounter = int(f.read())
        print("ファイル数は: " + str(fileCounter))

    f = open('./input.txt', encoding="utf-8")
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()

    lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
    lines1 = trimingByMark(lines1, "、")
    lines1 = trimingByMark(lines1, "。")
    lines1 = trimingByMark(lines1, "！")
    lines1 = trimingByMark(lines1, "？")
    lines1 = [x for x in lines1 if x]


    """
    l = []
    for line in lines1:
        l.append(re.findall(".*?、|.*$", line))

    l = flatten_with_any_depth(l)
    tmp = []
    for j in l:
        tmp.append(re.findall(".*?、|.*$", j))
    l = flatten_with_any_depth(tmp)

    
    """
    print([x for x in lines1 if x])

"""
    if (i != '') or (i != ' '):
        path_w = "./output/voice_" + str(fileCounter) + ".txt"
        with open(path_w, mode='w',encoding="utf-8") as f:
            f.write(str(i))
            fileCounter = fileCounter + 1
    
with open("./counter.txt", mode='w') as f:
    f.write(str(fileCounter))
"""
if __name__ == '__main__':
    main()