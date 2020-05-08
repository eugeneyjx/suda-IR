import re

def readfile(fname):
    with open(fname,encoding='utf-8') as f:
        data=f.readlines()
        textlist=[]
        for i in data:
            textlist.append(re.sub(r'\n', '', i))
    return textlist

def matchpart(textlist):
    r=re.compile(r'<.*?>',re.I|re.M|re.S)
    textlist=list(map(lambda x:r.sub("",x),textlist))
    while "" in textlist:
        textlist.remove("")
    return textlist

def getanchor1(text):
    r=re.compile(r'<a href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    halflist=list(r.findall(text))
    return halflist

def getanchor2(text):
    r=re.compile(r'<a target="_blank" href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    halflist=list(r.findall(text))
    return halflist

def output(textlist,halflist,fname):
    with open(fname, 'w',encoding='UTF-8') as f:
        f.write("title:\n")
        f.write(textlist[0])
        f.write("\nbody:\n")
        f.write(("").join(textlist[1::]))
        f.write("\nlink:\n")
        for i in halflist:
            f.write("%-25s" % str(i[1]))
            f.write(str(i[0]) + '\n')
            f.write('\n')

if __name__ == '__main__':
    textlist=readfile("1.html")
    print(textlist)
    contextlist=matchpart(textlist)
    print(contextlist)
    context=("").join(textlist)
    halflist=getanchor1(context)
    output(contextlist,halflist,"result.txt")