import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file="post.xlsx"
xl=pd.ExcelFile(file)
# dfs = pd.read_excel('post.xlsx')
dfs=xl.parse(xl.sheet_names[0])#excel to df
dfs=list(dfs['Your posts'])
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="updated"
str3="Updated"
str4="Generated"
str2="posted"
for x in dfs:
    a=x.find(str1)
    b=x.find(str2)
    c = x.find(str3)
    d = x.find(str4)
    e=x.find(":")

    if a==-1 and b==-1 and c==-1 and d==-1 and e==-1:
        print(x)
        ss=sid.polarity_scores(x)
        for k in ss:
            print(k,ss[k])





