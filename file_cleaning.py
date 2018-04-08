# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:26:39 2018

@author: Manoj
"""

import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import calendar

wordnet = WordNetLemmatizer()
punct = string.punctuation
stopword = stopwords.words('english')

def clean_query(file):   
    infile = pd.read_excel(file)    
    query_series = infile['QueryText']
    #print(query_series.head(15))    
    query_series = query_series.apply(lambda x: ' '.join([wordnet.lemmatize(word) for word in x.split() if word.lower() not in stopword]))
    query_series = query_series.apply(lambda x: ''.join([char for char in x if char not in punct]))
    #print(query_series.head(15))
    infile['QueryText'] = query_series
    infile['CreatedOn'] = pd.to_datetime(infile['CreatedOn'])
    infile['CreatedYear']= infile['CreatedOn'].dt.year
    infile['CreatedMonth'] = infile['CreatedOn'].dt.month.apply(lambda x: calendar.month_abbr[x])
    print(infile.head())
    
    infile.to_excel('cleaned_series.xlsx',index=False)

clean_query("C:\\Users\\Manoj\\Desktop\\Nasscom\\hackathon\\cleaned_df.xlsx")



