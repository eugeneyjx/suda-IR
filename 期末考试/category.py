import jieba
import re
import math
import time


def gendata():
    with open("raw_data.txt",encoding="utf-8") as f:
        data = f.readlines()
    return data

def genres():
    with open("raw_data.txt",encoding="utf-8") as f:
        data = f.readlines()
    res = []
    for i in data:
        i = re.sub(r"(\n)|( +)", "", i)
        res.append(list(jieba.cut(i)))
    for i in res:
        if i == []:
            res.remove(i)  # 分词
    resdict=dict(zip(range(len(res)),res))
    return resdict

def genqres():
    with open("query.txt",encoding='utf-8') as f:
        querybase = f.readlines()
    qres = []
    for i in querybase:
        i = re.sub(r"(\n)|( +)", "", i)
        qres.append(list(jieba.cut(i)))
    for i in qres:
        if i == []:
            qres.remove(i)  # 分词
    print("qres", qres)
    return qres

def genvs(res):
    vs = []
    vs += [j for i in res.values() for j in i]
    vs = set(vs)
    print('vslen',len(vs))
    return vs  # 求出VS

def genidf(res,vs):
    dictidf=dict()
    for i in vs:
        dictidf[i]=0
    count=0
    for i in vs:
        for j in res:
            if i in res[j]:
                dictidf[i] += 1
        count+=1
        print("idftemplen",count,'/',len(vs))
    return dictidf

def filtervs(idftemp,vs):
    print("vslen", len(vs))
    for i in idftemp.keys():
        if idftemp[i]==1:
            vs.remove(i)
            print("vslen", len(vs))
    return vs

def filteridf(idftemp):
    idf=dict()
    for i in idftemp:
        if idftemp[i]!=1:
            idf[i]=1 / idftemp[i]
            print("idflen", len(idf))
    return idf

def gentf(doc,vs):
    tf=dict()
    for i in vs:
        if doc.count(i)!=0:
            tf[i]=(doc.count(i) / len(doc))
            print("tflen",len(tf),'/',len(vs))
    return tf # 求出TF

def genvec(tf,idf):
    vec=dict()
    inter=set(tf.keys())&(set(idf.keys()))
    for i in inter:
        vec[i]=tf[i] * idf[i]
        print("veclen",len(vec))
    return vec

def sims(vec1,vec2):
    sim = 0
    len1, len2 = 0, 0
    inter=set(vec1.keys())&(set(vec2.keys()))
    for i in inter:
        sim += vec1[i] * vec2[i]
    for i in vec1:
        len1 += vec1[i] ** 2
    for i in vec2:
        len2 += vec2[i] ** 2
    len1, len2 = math.sqrt(len1), math.sqrt(len2)
    sim /= len1 * len2   #求出相似度
    return sim

def gentf2dict(idf):
    tf2dict=dict()
    for i in res:
        tf2dict[i]=gentf(res[i],vs)
    return tf2dict

def genvec2dict(tf2dict):
    vec2dict = dict()
    for i in res:
        vec2dict[i]=genvec(tf2dict[i],idf)
    return vec2dict

def gensim(vec1, res, simbase, c, vec2dict):
    count=0
    for i in res:
        sim = sims(vec1,vec2dict[i])
        simbase.append(sim)
        count+=1
        print('sim',count+(c*1000),'/',len(res)+(c*1000))


if __name__ == "__main__":
    start=time.time()
    qres=genqres()
    data=gendata()
    res=genres()
    vs = genvs(res)
    idftemp = genidf(res, vs)
    vs = filtervs(idftemp, vs)
    idf = filteridf(idftemp)
    with open("idf keys.txt", 'w',encoding="utf-8") as f:
        for i in idf:
            f.write(str(i))
            f.write('\n')
    with open("idf values.txt", 'w',encoding="utf-8") as f:
        for i in idf:
            f.write(str(idf[i]))
            f.write('\n')

    tf2dict=gentf2dict(idf)
    vec2dict=genvec2dict(tf2dict)
    with open("tf2dict.txt", "w",encoding="utf-8") as f:
        for i in tf2dict:
            f.write(str(tf2dict[i]))
            f.write("\n")
    with open("vec2dict.txt", "w",encoding="utf-8") as f:
        for i in vec2dict:
            f.write(str(vec2dict[i]))
            f.write("\n")

    # result = []
    # c=0
    # for i in range(len(qres)):
    #     result.append([])
    # for query in qres[1:]:
    #     tf1 = gentf(query, vs)
    #     vec1 = genvec(tf1, idf)
    #     simbase=[]
    #     gensim(vec1, res, simbase, c, vec2dict)
    #     print("datalen=", len(data), "simbaselen=", len(simbase))
    #     sortbase = []
    #     for i in range(len(data)):
    #         sortbase.append([data[i], simbase[i]])
    #     sortbase.sort(key=lambda x: x[1], reverse=True)
    #
    #     for i in range(10):
    #         result[c].append(sortbase[i][0])
    #     c+=1
    #
    # with open("myresult.txt","w",encoding='utf-8') as f:
    #     for i in range(len(qres)):
    #         f.write("Query")
    #         f.writelines(qres[i])
    #         f.write("\n\n")
    #         for k in result[i]:
    #             f.write(str(k))
    #             f.write('\n')
    #         f.write('\n')

    end=time.time()
    print("time=",end-start)
