with open("Out.txt",) as f:
    data1=f.readlines()
with open("result.txt",encoding='utf-8') as f:
    data2=f.readlines()
for i in range(len(data1)):
    if data1[i]!=data2[i]:
        print(data1[i])
        print(data2[i])
        print(i)