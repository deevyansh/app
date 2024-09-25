import streamlit as st
import pandas as pd
from Pages.globals import insert, get

st.title("Check Dates")
df=pd.read_csv(f"""Data/{get("user")}.csv""")
df=df[['hour','date','month','value']]
df=df.sort_values(['month','date','hour'])
df=df.reset_index(drop=True)

df['month']=df['month'].astype(int)
df['hour']=df['hour'].astype(int)
df['date']=df['date'].astype(int)

st.table(df)
