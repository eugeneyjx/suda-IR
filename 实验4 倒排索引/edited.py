import re


def indoc():
    docs = {}
    for i in range(1, 10):
        fname = "d" + str(i) + ".txt"
        with open(fname, encoding="utf-8") as f:
            data = f.readlines()
        words = []
        for j in data:
            words += (re.sub(r'\n', '', j)).lower().split(' ')
        docs[i] = words
    return docs

def getindex(docs):
    index = {}
    for i in docs:
        for j in docs[i]:
            if j not in index:
                index[j] = []
                index[j].append(i)
            else:
                if i in index[j]:
                    continue
                else:
                    index[j].append(i)
    return index

def getdict(index,df):
    with open("dict.index","w",encoding="utf-8") as f:
        for i in sorted(index.keys()):
            f.write(i)
            f.write("\t")
            f.write(str(df[i]))
            f.write("\t")
            for j in index[i]:
                f.write(str(j))
                f.write(" ")
            f.write("\n")
        print("输出完成")

if __name__=="__main__":
    docs=indoc()
    index=getindex(docs)
    indexs=[]
    fre={}
    for i in index:
        fre[i]=len(index[i])
    getdict(index,fre)
    while 1:
        q1=input("请输入查询内容1:")
        bools=input("请输入AND或OR，不输入则只检索第一个单词:")
        if bools=="":
            if q1 not in index:
                res=None
                print(res)
            else:
                res=index[q1]
                print(res)
        elif bools=="AND":
            q2=input("请输入查询内容2:")
            if q1 not in index or q2 not in index:
                res=None
                print(res)
            else:
                res=list(set(index[q1]).intersection(set(index[q2])))
                for i in res:
                    print(i)
                    print(" ")
        else:
            q2=input("请输入查询内容2:")
            if q1 not in index and q2 not in index:
                res=None
                print(res)
            else:
                res=list(set(index[q1]).union(set(index[q2])))
                for i in res:
                    print(i)
                    print(" ")
