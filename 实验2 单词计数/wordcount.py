import re
def inputwords(path):
    with open(path, encoding='utf-8') as f:
        data = f.readlines()
        words = []
        for i in data:
            words+=(re.sub(r'\n', '', i)).lower().split(' ')
    return words

def getdict(words):
    dic={}
    for i in words:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic

def outputdic(dic):
    with open("dict.index","w") as f:
        for key in dic:
            f.write(key)
            f.write('\t')
            f.write(str(dic[key]))
            f.write('\n')


if __name__=="__main__":
    words=inputwords("sample-en.txt")
    dic=getdict(words)
    outputdic(dic)
    print("dict.index生成成功。")

    while(1):
        query = input("用户请输入：")
        if query=="###":
            print("程序退出")
            break
        if query in dic:
            print("出现的次数：",dic[query])
        else:
            print("出现的次数：","0")
