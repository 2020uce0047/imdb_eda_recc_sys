# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np


df = pd.read_csv('imdb_top_1000.csv')
df = df.drop(columns = ['Poster_Link'])

#Duration column in min
duration = df['Runtime'].apply(lambda x: x.split(' ')[0])
df['Duration(min)'] = duration
df['Duration(min)'].astype(int)
df = df.drop(columns = ['Runtime'])

# Splitting multiple genre
value_count_genre = df['Genre'].apply(lambda x: len(x.split(',')))
print(max(value_count_genre))
Genre1 = df['Genre'].apply(lambda x: x.split(',')[0])
Genre2 = df['Genre'].apply(lambda x: x.split(',')[1] if len(x.split(','))==2 else '')
Genre3 = df['Genre'].apply(lambda x: x.split(',')[2] if len(x.split(','))==3 else '')

df['Genre1'] = Genre1
df['Genre2'] = Genre2
df['Genre3'] = Genre3
df = df.drop(columns = 'Genre')

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


