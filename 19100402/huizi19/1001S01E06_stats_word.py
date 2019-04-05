
import  re   

#英文单词统计函数
def  stats_text_en(text):
    a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
    str=a.split()                      #单词划分
    wordcount={}
    for i in str:             
        wordcount[i]=str.count(i)     #词频统计词典设置
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)    #词频统计，按词频降序排列
    print(wordcount) #输出英文单词频数统计结果
  


#中文词频统计函数
import jieba

def  stats_text_cn(text):
    p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    res = re.findall(p, text)   #取中文
    result = ''.join(res)       #中文拼接
    cn=list(jieba.cut(result))   #结巴分词
    wordcount={}                 #词频统计字典初始化
    for i in cn:             
        wordcount[i]=cn.count(i)     #词频统计词典设置
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)    #词频统计，按词频降序排列
    print(wordcount)  #输出中文分词后的词频统计结果
    

