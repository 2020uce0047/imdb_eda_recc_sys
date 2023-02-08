import streamlit as st
import pandas as pd
import numpy as np
from Data_Cleaning import df 

st.title('Filmstars genre and rating')
#Default
stars = list(df['Star1'].values)+list(df['Star2'].values)+list(df['Star1'].values)
stars = np.unique(np.array(stars))
columns = ['Drama', 'Crime',
       'Action', 'Adventure', 'Biography', 'History', 'Sci-Fi', 'Romance',
       'Western', 'Fantasy', 'Comedy', 'Thriller', 'Animation', 'Family',
       'War', 'Mystery', 'Music', 'Horror', 'Musical', 'Film-Noir', 'Sport',
       'Other']
chart_data = df[columns].T
chart_data.rename(columns = {i:'Genre' for i in chart_data.columns}, inplace = True)
hist_values = pd.DataFrame(np.histogram(df.IMDB_Rating)).T.drop(columns = [1]).fillna(0)
hist_values.index = np.histogram(df.IMDB_Rating)[1]

star_name = st.multiselect('Star', options = stars, default = None)
if len(star_name)>0:
    chart_data = pd.DataFrame(index = columns)
    for i in star_name:
        df_star = df[df['Star1'].isin([i]) | df['Star2'].isin([i]) | df['Star3'].isin([i])][columns]
        bar_len = []
        for j in df_star.columns:  
            if 1 in df_star[j].value_counts().keys().to_list():
                bar_len.append(df_star[j].value_counts()[1])
            else: bar_len.append(0)
        chart_data[i] = bar_len
        


    # st.subheader('Number of pickups by hour')
#     hist_values = np.histogram(
#         df[df['Star1'].isin(star_name) | df['Star2'].isin(star_name) | df['Star3'].isin(star_name)].IMDB_Rating, bins=24, range=(0,10))[0]

st.bar_chart(data = chart_data)
# st.bar_chart(data = hist_values)