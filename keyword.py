
# from nltk.corpus import stopwords 

f=open("./stopwords.txt", 'r', encoding='UTF8')


# file = open("result.txt", 'r', encoding='UTF8')
stopwords=[]

while True:
    line = f.readline()
    if not line: break

    if line[len(line)-1:] =="\n":
        line = line[:len(line)-1]
    stopwords.append(line)


print(stopwords)