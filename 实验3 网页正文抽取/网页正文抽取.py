import re
import pickle

def read_file_a(fin_name):
    with open(fin_name,'r',encoding='UTF-8') as f:
        text_list=f.readlines()
        text_list=list(map(lambda x:x.strip('\n\t'),text_list))
        while ("")in text_list:
            text_list.remove("")
        text_list=list(map(lambda x:x+"\n",text_list))
    return text_list

def get_title(fin_name):
    with open(fin_name, 'r', encoding='UTF-8') as f:
        text_list = f.readlines()
        text_list = list(map(lambda x: x.strip('\n\t'), text_list))
        str_a=("").join(text_list)
        r1 = re.compile(r'>(.*?)<', re.I | re.M | re.S)
        list_a=list(r1.findall(str_a))
        while ("")in text_list:
            text_list.remove("")
    return list_a




def read_file_b(fin_name):
    with open(fin_name,'r',encoding='GB2312') as f:
        text_list=f.readlines()
        text_list=list(map(lambda x:x.strip(),text_list))
    return text_list

def get_main_article(str_list):
    r1=re.compile(r'''<.*?>''',re.I|re.M|re.S)
    str_a=str(r1.sub("",("").join(str_list)))
    return str_a

def get_anchor_acticle1(str_a):
    r2=re.compile(r'<a href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    half_list=list(r2.findall(str_a))
    return half_list
def get_anchor_acticle2(str_a):
    r2=re.compile(r'<a target="_blank" href="(.*?)">(.*?)</a>',re.I|re.M|re.S)
    half_list=list(r2.findall(str_a))
    return half_list

def writeTxt_a(dataList_1,dataList_2, fileName):
    f = open(fileName, 'w',encoding='UTF-8')
    f.write("title:\n")
    f.write(dataList_1[0])
    f.write("\nbody:\n")
    f.write(("").join(dataList_1[1::]))
    f.write("\nlink:\n")
    for ele in dataList_2:
        length = len(ele)
        f.write("%-25s"%str(ele[length - 1]))
        for i in range(length-1):
            f.write(str(ele[i])+'\t')
        f.write('\n')

def writeTxt_b(dataList_1,dataList_2, fileName):
    f = open(fileName, 'w',encoding='GB2312')
    f.write("title:\n")
    f.write(dataList_1[0])
    f.write("\nbody:\n")
    f.write(("").join(dataList_1[1::]))
    f.write("\nlink:\n")
    for ele in dataList_2:
        length = len(ele)
        f.write("%-25s"%str(ele[length - 1]))
        for i in range(length-1):
            f.write(str(ele[i])+'\t')
        f.write('\n')


if __name__ == '__main__':
    str_list2=read_file_a("2.html")
    str_2=get_main_article(str_list2)
    half_list2=get_anchor_acticle2(str(("").join(str_list2)))
    str_list1 = read_file_a("1.html")
    str_1 = get_main_article(str_list1)
    half_list1 = get_anchor_acticle1(str(("").join(str_list1)))
    # str_list3 = read_file_a("d:\\3.html")
    # str_3 = get_main_article(str_list3)
    # half_list3= get_anchor_acticle1(str(("").join(str_list3)))
    # str_list4 = read_file_a("d:\\4.html")
    # str_4 = get_main_article(str_list4)
    # half_list4 = get_anchor_acticle1(str(("").join(str_list4)))
    writeTxt_a(str_1,half_list1,"1.txt")
    writeTxt_a(str_2,half_list2,"2.txt")
    # writeTxt_a(str_3, half_list3, "d:\\3.txt")
    # writeTxt_a(str_4, half_list4, "d:\\4.txt")
