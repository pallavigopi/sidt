import pandas as pd
import string
import re
import nltk

def preprocess(df):
    df['Tweets'] = df['Tweets'].apply(lambda x: remove_mentions(x))
    df['Tweets'] = df['Tweets'].apply(lambda x: remove_punct(x))
    df['Tweets'] = df['Tweets'].apply(lambda x: remove_url(x))
    print("\nPre Processed")
    # print(df[['Tweets'].head(10))


def remove_url(text):
    text  = "".join([char for char in text])
    text = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
    return text


def remove_mentions(text):
  text = "".join([char for char in text])
  text = re.sub(r'@(\w+)', '', text, flags=re.MULTILINE)
  return text

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


def tokenization(text):
    text = re.split('\W+', text)
    return text


# nltk.download('words')
engwords = nltk.corpus.words.words()
def remove_words(text):
    text = [word for word in text if word in engwords]
    return text
    

# nltk.download('stopwords')
stopword = nltk.corpus.stopwords.words('english')
def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text
    