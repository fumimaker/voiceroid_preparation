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
    f = open('./input.txt', encoding="utf-8")
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    print()
    print("///////////////////////////////")
    print("inputファイル読み込み完了")
    print(str(len(data1))+"文字解析開始...")
    print("///////////////////////////////")
    print()

    text = data1
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    text = text.strip()
    data1 = text

    print()
    print("///////////////////////////////")
    print("ルビ除去完了...構文解析開始...")
    print("///////////////////////////////")
    print()

    lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
    lines1 = trimingByMark(lines1, "、")
    lines1 = trimingByMark(lines1, "。")
    lines1 = trimingByMark(lines1, "！")
    lines1 = trimingByMark(lines1, "？")
    lines1 = [x for x in lines1 if x]
    
    for word in lines1:
        if "、" in word: # iは文字列
            if len(word) + len(lines1[lines1.index(word)+1]) < 30:
                lines1[lines1.index(word)] = lines1[lines1.index(word)] + lines1[lines1.index(word)+1]
    
    
    for word in lines1:
        print(word)

    print()
    print()
    print(str(len(lines1))+"テキスト分の解析完了")

    with open("./counter.txt", mode='r') as f:
        fileCounter = int(f.read())
        print()
        print()
        print("すでにあるファイル数: " + str(fileCounter))

    print()
    print()
    print("///////////////////////////////")
    print("保存開始...")
    print("///////////////////////////////")
    print()
    print()

    for word in lines1:
        path_w = "./output/voice_" + str(fileCounter) + ".txt"
        with open(path_w, mode='w',encoding="utf-8") as f:
            f.write(str(word))
            fileCounter = fileCounter + 1
    
    with open("./counter.txt", mode='w') as f:
        f.write(str(fileCounter))

    print()
    print()
    print("保存終了")


if __name__ == '__main__':
    main()