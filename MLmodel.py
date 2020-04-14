import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

    
def findCategory(df):
    vect = pickle.load(open('CV.pkl', 'rb'))
    model = pickle.load(open('Finalmodel.pkl', 'rb'))
    df['Category']=model.predict(vect.transform(df['Tweets']))
    majority=df['Category'].value_counts().idxmax()
    classification={0:"Safe To Ignore",1:"Concerned",2:"Strongly Concerned"}
    df['Category']=[classification[item] for item in df['Category']]
    l=df['Category'].value_counts()
    categoryarr = l.to_dict()
    print("Category")
    print(Category1(majority))
    return categoryarr,majority


def Category1(x):
  if(x==0):
    return "Safe To Ignore"
  elif(x==1):
    return "Concerned"
  elif(x==2):
    return "Strongly Concerned"


