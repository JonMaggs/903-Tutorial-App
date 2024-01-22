import pandas as pd

def read_data(filepath):
    """
    Reads in a CSV from filepath and returns dataframe for analysis.

    Inputs:
    filepath: -> str: path to csv

    Outputs:
    df -> Dataframe: Datafram for analysis

    """
    df = pd.read_csv(filepath)
    return df

def ingress(df):
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    return df

def gender_count(df):
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    return len(df['CHILD'].unique())
