# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np


df = pd.read_csv('imdb_top_1000.csv')
df = df.drop(columns = ['Poster_Link'])


#Duration in min
duration = df['Runtime'].apply(lambda x: x.split(' ')[0])
df['Duration(min)'] = duration
df['Duration(min)'].astype(int)
df = df.drop(columns = ['Runtime'])


#Make the values of Gross column integral
df['Gross'] = df['Gross'].str.replace(',', '')
df['Gross'].fillna(0, inplace = True)
df['Gross'].astype(int)


#Replace null values by 'na'
for i in df.columns:
  if(df[i].dtype == object):
    df[i].fillna('na', inplace = True)


#Extract unique genres of the movies
gen_unique = []
for genre in df['Genre']:
    t = len(genre.split(', '))
    for j in range(t):
        if genre.split(', ')[j] not in gen_unique:
            gen_unique.append(genre.split(', ')[j])  
if('Other' not in gen_unique):
    gen_unique.append('Other')

#Create columns for each unique genre
k = 'default'            
def check_genre(genre):
    t = len(genre.split(', '))
    for j in range(t):
        if genre.split(', ')[j] == k:
            return 1
    else:
        return 0
for i in gen_unique:
    k = i
    df[i] = df['Genre'].apply(check_genre)    

#Dropping movies with certificate having value count(s) < 10
unique_cert = df['Certificate'].value_counts()
print(unique_cert)

df = df.drop(df[(df['Certificate'] == 'TV-PG') |
                (df['Certificate'] == 'GP') |
                (df['Certificate'] == 'TV-14') |
                (df['Certificate'] == '16') |
                (df['Certificate'] == 'TV-MA') |
                (df['Certificate'] == 'Unrated') |
                (df['Certificate'] == 'U/A')].index)

#Saving the cleaning dataset
df.to_csv('imdb_top_1000_cleaned.csv', index = False)
