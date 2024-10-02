import streamlit as st
import pandas as pd
from Pages.globals import insert, get
import os

st.title("Check Dates")
if(os.path.exists(f"""Data/{get("user")}.csv""")):
    df=pd.read_csv(f"""Data/{get("user")}.csv""")
else :
    df=pd.read_csv("Data/NO.csv")
df=df[['hour','date','month','value']]
df=df.sort_values(['month','date','hour'])
df=df.reset_index(drop=True)

df['month']=df['month'].astype(int)
df['hour']=df['hour'].astype(int)
df['date']=df['date'].astype(int)

st.table(df)
