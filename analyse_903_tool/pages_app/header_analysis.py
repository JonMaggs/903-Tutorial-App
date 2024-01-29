import pandas as pd
import streamlit as st
import numpy as np
import json
import plotly.express as px

#https://docs.streamlit.io/library/api-reference/write-magic/st.write

def ingress(df):
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')
    df['AGE'] = pd.to_datetime('today').normalize() - df['DOB']
    df['AGE'] = (df['AGE'] / np.timedelta64(1, 'Y')).astype('int')
    return df

def gender_count(df):
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    return len(df['CHILD'].unique())

st.title('903 Header Analysis App')

upload = st.file_uploader("Upload 903 Header File")

if upload:
    
    df = pd.read_csv(upload)

    with st.sidebar:
        ethnicities = st.sidebar.multiselect(
            'Select ethnicities for analysis',
            df['ETHNIC'].unique(),
            df['ETHNIC'].unique()
        )

    df = df[df['ETHNIC'].isin(ethnicities)]
    
    df = ingress(df)
    child_pop = child_count(df)
    male, female = gender_count(df)
    average_age = round(df['AGE'].mean())

    st.write(f'The total population of children is: {child_pop}')
    st.write(f'The total number of males is: {male}')
    st.write(f'The total number of females is: {female}')
    st.write(f'The avergae age is: {average_age}')

    gender_bar = px.bar(df,
                        x='SEX',
                        title='Number of children of each sex in 903 data',
                        labels={'SEX':'Sex',
                                'count':'Number of children'})
    st.plotly_chart(gender_bar)

    ethnicity_bar = px.bar(df,
                        x='ETHNIC',
                        title='Number of children of each ethnicity in 903 data',
                        labels={'ETHNIC':'Ethnicity',
                                'count':'Number of children'})
    st.plotly_chart(ethnicity_bar)

    age_histo = px.histogram(df,
                             x="AGE",
                              title='Number of children of each Age in 903 data',
                        labels={'AGE':'Age',
                                'count':'Number of children'})
    st.plotly_chart(age_histo)

    st.dataframe(df)

