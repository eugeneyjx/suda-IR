import re

def intext(fname):
    with open(fname,encoding='utf-8') as f:
        data=f.readlines()
        alist=[]
        for i in data:
            alist.append(re.sub(r'\n', '', i))
    return alist

def getmain(alist):
    r1=re.compile(r'<.*?>',re.I|re.M|re.S)
    alist=list(map(lambda x:r1.sub("",x),alist))
    while "" in alist:
        alist.remove("")
    return alist

def getanchor1(txt):
    r=re.compile(r'<a href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    hrl=list(r.findall(txt))
    return hrl

def getanchor2(txt):
    r=re.compile(r'<a target="_blank" href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    hrl=list(r.findall(txt))
    return hrl

def output(alist,hrl,fname):
    with open(fname, 'w',encoding='UTF-8') as f:
        f.write("title:\n")
        f.write(alist[0])
        f.write("\nbody:\n")
        f.write(("").join(alist[1::]))
        f.write("\nlink:\n")
        for i in hrl:
            f.write(str(i[1]))
            f.write(str(i[0]) + '\n')
            f.write('\n')

if __name__ == '__main__':
    alist=intext("1.html")
    blist=getmain(alist)
    txt=("").join(blist)
    hrl=getanchor1(txt)
    output(blist,hrl,"result.txt")