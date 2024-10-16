import streamlit as st
import pandas as pd
import os
from Pages.globals import insert, get
from db import is_there, storethedata

st.title("Fast Bidding")
input=st.date_input("Bidding Date")
date=input.day
year=input.year
month=input.month

price=st.number_input("Price")
Quantity=st.number_input("Quantity")

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

df = df.loc[(df["month"] == int(month)) & (df["date"] == int(date))]

l=[]
for i, row in df.iterrows():
    l.append("Hour:" + str(int(row["hour"])) + " Prescribed Quantity(in kWh):" + str(row["value"]))
result=st.radio("Select the Hour",l)

if(st.button("Final the Bid")):
    p=True
    hour = int(float(result.split("Hour:")[1].split(" Prescribed Quantity")[0]))
    Obj1 = [get("user"), year, month, date, hour]
    Obj2 = ["admin",year,month, date, hour]
    if (is_there(Obj1)):
        p = False
        st.error("Bids are colliding with the previous done Bids")
    if (is_there(Obj2)):
        p = False
        st.error("Market is already cleared for this hour")

    if(p):
        st.success("Bids Submitted Successfully")
        Obj = {"User": get("user"),
               "Quantity": Quantity,
               "Price": price,
               "Date": date,
               "Month": month,
               "Year": year,
               "Hour": hour,
               "State": "Waiting"}
        storethedata("Bids", Obj)












