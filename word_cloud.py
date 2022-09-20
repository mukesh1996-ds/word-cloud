# Loading all the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud, STOPWORDS

# Loading the dataset
df = pd.read_csv('twitterdata.csv')

# checking weather data load without error
print(df.head(2))   

# Converting caption text to upper case
print(df['text'].str.upper().head())

# Printing the first caption
print(df['text'][0])

# Applying regex on text data and transforming it
df['text_new'] = ''
for i in range(len(df['text'])):
    m = re.search('(?<=:)(.*)', df['text'][i])
    try:
        df['text_new'][i]=m.group(0)
    except AttributeError:
        df['text_new'][i]=df['text'][i]
        
print(df['text_new'])

def wordcloud_by_province(dataset):
    stopwords = set(STOPWORDS)
    stopwords.add("https")
    stopwords.add("00A0")
    stopwords.add("00BD")
    stopwords.add("00B8")
    stopwords.add("ed")
    stopwords.add("demonetization")
    stopwords.add("Demonetization co")
    #Narendra Modi is the Prime minister of India
    stopwords.add("lakh")
    wordcloud = WordCloud(background_color="white",
                          stopwords=stopwords,
                          random_state = 2016).generate(" ".join([i for i in dataset['text_new'].str.upper()]))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("Demonetization")

wordcloud_by_province(df)  