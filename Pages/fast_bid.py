import streamlit as st
import pandas as pd
import os
from Pages.globals import insert, get
from db import is_there, storethedata
st.title("Fast Bidding")
main_option=st.radio("How many bids you want to make", ["Single","Multiple"])

if(main_option=="Single"):
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
        prescribed_quantity = int(float(result.split("Prescribed Quantity(in kWh):")[1]))
        if (is_there(Obj1)):
            p = False
            st.error("Bids are colliding with the previous done Bids")
        if (is_there(Obj2)):
            p = False
            st.error("Market is already cleared for this hour")

        if(Quantity<0 or Quantity>prescribed_quantity):
            st.error("Please enter a valid quantity")

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

else:
    input = st.date_input("Bidding Date")
    date = input.day
    year = input.year
    month = input.month

    price1 = st.number_input("Price 1")
    Quantity1 = st.number_input("Quantity 1")
    price2 = st.number_input("Price 2")
    Quantity2 = st.number_input("Quantity 2")
    price3 = st.number_input("Price 3")
    Quantity3 = st.number_input("Quantity 3")


    if (os.path.exists(f"""Data/{get("user")}.csv""")):
        df = pd.read_csv(f"""Data/{get("user")}.csv""")
    else:
        df = pd.read_csv("Data/NO.csv")


    df = df[['hour', 'date', 'month', 'value']]
    df = df.sort_values(['month', 'date', 'hour'])
    df = df.reset_index(drop=True)

    df['month'] = df['month'].astype(int)
    df['hour'] = df['hour'].astype(int)
    df['date'] = df['date'].astype(int)

    df = df.loc[(df["month"] == int(month)) & (df["date"] == int(date))]

    l = []
    for i, row in df.iterrows():
        l.append("Hour:" + str(int(row["hour"])) + " Prescribed Quantity(in kWh):" + str(row["value"]))


    selected_hours = []
    quantities=[Quantity1,Quantity2,Quantity3]
    prices=[price1,price2,price3]
    for i in l:
        if st.checkbox(i):
            selected_hours.append(i)


    if (st.button("Final the Bid")):
        p = True
        for i in range(len(selected_hours)):
            hour = int(float(selected_hours[i].split("Hour:")[1].split(" Prescribed Quantity")[0]))
            Obj1 = [get("user"), year, month, date, hour]
            Obj2 = ["admin", year, month, date, hour]
            prescribed_quantity = (float(selected_hours[i].split("Prescribed Quantity(in kWh):")[1]))
            if (is_there(Obj1)):
                p = False
                st.error("Bids are colliding with the previous done Bids")
            if (is_there(Obj2)):
                p = False
                st.error("Market is already cleared for this hour")

            if (quantities[i] < 0 or quantities[i]> prescribed_quantity):
                p=False
                st.error("Please enter a valid quantity")

        if (p):
            st.success("Bid Submitted Successfully")
            for i in range(len(selected_hours)):
                Obj = {"User": get("user"),
                       "Quantity": quantities[i],
                       "Price": prices[i],
                       "Date": date,
                       "Month": month,
                       "Year": year,
                       "Hour": hour,
                       "State": "Waiting"}
                storethedata("Bids", Obj)













