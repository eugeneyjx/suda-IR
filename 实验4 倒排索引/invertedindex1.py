import re

class Stats:
    def __init__(self,num):
        self.head=num
        self.next=None


class Index:
    def __init__(self):
        self.head=None
        self.next=None

    def append(self,new_data):
        if self.head==None:
            self.head=Stats(new_data)
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=Stats(new_data)

    def show(self):
        cur=self.head
        while cur!=None:
            print(cur.head,end=' ')
            cur=cur.next


def inputdoc():
    docpool={}
    for i in range(1,10):
        filename="d"+str(i)+".txt"
        with open(filename,encoding="utf-8") as f:
            data = f.readlines()
        words = []
        for j in data:
            words += (re.sub(r'\n', '', j)).lower().split(' ')
        docpool[i]=words
    return docpool

def constructindex(docpool):
    index={}
    for i in docpool:
        for j in docpool[i]:
            if j not in index:
                index[j]=[]
                index[j].append(i)
            else:
                if i in index[j]:
                    continue
                else:
                    index[j].append(i)
    return index

def outputdict(index,df):
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

if __name__=="__main__":
    docpool=inputdoc()
    index=constructindex(docpool)
    indexpool=[]
    df={}
    for i in index:
        df[i]=len(index[i])
    for i in index:
        A=Index()
        A.append(i)
        A.append(df[i])
        for j in index[i]:
            A.append(j)
        indexpool.append(A)
    print(indexpool)
    for i in indexpool:
        i.show()
        print()
    outputdict(index,df)
    while 1:
        query1=input("请输入查询内容1:")
        bools=input("请输入AND或OR，不输入则只检索查询内容1:")
        if bools=="":
            if query1 not in index:
                result=None
                print(result)
            else:
                result=index[query1]
                print(result)
        elif bools=="AND":
            query2=input("请输入查询内容2:")
            if query1 not in index or query2 not in index:
                result=None
                print(result)
            else:
                result=list(set(index[query1]).intersection(set(index[query2])))
                for i in result:
                    print(i)
                    print(" ")
        else:
            query2=input("请输入查询内容2:")
            if query1 not in index and query2 not in index:
                result=None
                print(result)
            else:
                result=list(set(index[query1]).union(set(index[query2])))
                for i in result:
                    print(i)
                    print(" ")

        termi=input("输入###退出查询")
        if termi=="###":
            break