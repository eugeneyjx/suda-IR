import re

def inputsen(path):
    with open(path, encoding='utf-8') as f:
        data = f.readlines()
        sentences = []
        for i in data:
            sentences.append(re.sub(r'(\n)|(\ufeff)', '', i))
    return sentences

def inputdict(path):
    with open(path,encoding='utf-8') as f:
        data=f.readlines()
        dic=set()
        for i in data:
            dic.add(re.sub(r'(\n)','',i))
    return dic

def segmatch(sen,dic):
    n=len(sen)
    i=0
    result=[]
    while(i<n):
        for j in range(n,i,-1):
            if sen[i:j] in dic:
                result.append(sen[i:j])
                i=j
                break
        else:
            result.append(sen[i:i+1])
            i+=1

    return result

def outputresult(resultpool):
    with open("result.txt","w",encoding="utf-8") as f:
        for result in resultpool:
            for word in result:
                f.write(word)
                f.write(" ")
            if result!=resultpool[-1]:
                f.write("\n")

def evaluate():
    with open("Answer.txt",encoding='utf-8') as f:
        data = f.readlines()
    temp = []
    Answerspool=[]
    for i in data:
        temp.append(re.sub(r'\n', '', i))
    for i in temp:
        Answerspool.append(i.split(" "))
    for i in Answerspool:
        if '' in i:
            i.remove('')

    with open("result.txt",encoding='utf-8') as f:
        data = f.readlines()
    temp = []
    resultpool=[]
    for i in data:
        temp.append(re.sub(r'\n', '', i))
    for i in temp:
        resultpool.append(i.split(" "))
    for i in resultpool:
        if '' in i :
            i.remove('')

    n=len(Answerspool)
    cornum,idenum,existnum,wronum=0,0,0,0
    for i in range(n):
        count=0
        print(resultpool[i])
        print(Answerspool[i])
        for result in resultpool[i]:
            if result in Answerspool[i]:
                count+=1
        print(count,'/',len(Answerspool[i]))
        cornum+=count
        idenum+=len(resultpool[i])
        existnum+=len(Answerspool[i])

    P=cornum/idenum
    R=cornum/existnum
    F=P*R*2/(P+R)
    print("正确识别的词数：",cornum)
    print("识别出的总体个数：",idenum)
    print("测试集中的总体个数：",existnum)
    print("正确率：",P)
    print("召回率：",R)
    print("F值：",F)


if __name__=="__main__":
    dic=inputdict("Dict.txt")
    senbase=inputsen("Sentence.txt")
    resultpool=[]
    for sen in senbase:
        resultpool.append(segmatch(sen,dic))
    outputresult(resultpool)
    evaluate()