import streamlit as st
from Pages.globals import insert,get
import pandas as pd
from db import storethedata

st.subheader("Welcome")
st.write(get("user"))

Bid_Input=st.radio("How many bids you want to make", ["Single Bid", "Multiple Bid"])

l=[[],[],[]]#(Convention)- (Quantity, Price, Date , From hour, To hour)
quantity_widget1, price_widget1, date_widget1, from_widget1, to_widget1=st.columns([1,1,1,1,1])
l[0].append(quantity_widget1.number_input("Quantity1"))
l[0].append(price_widget1.number_input("Price1"))
l[0].append(date_widget1.date_input("Date1"))
l[0].append(from_widget1.number_input("From Hour1", min_value=0, max_value=23))
l[0].append(to_widget1.number_input("To Hour1", min_value=0, max_value=23))

if(Bid_Input=="Multiple Bid"):
    quantity_widget2, price_widget2, date_widget2, from_widget2, to_widget2 = st.columns([1, 1, 1, 1, 1])
    l[1].append(quantity_widget2.number_input("Quantity2"))
    l[1].append(price_widget2.number_input("Price2"))
    l[1].append(date_widget2.date_input("Date2"))
    l[1].append(from_widget2.number_input("From Hour2", min_value=0, max_value=23))
    l[1].append(to_widget2.number_input("To Hour2", min_value=0, max_value=23))

    quantity_widget3, price_widget3, date_widget3, from_widget3, to_widget3 = st.columns([1, 1, 1, 1, 1])
    l[2].append(quantity_widget3.number_input("Quantity3"))
    l[2].append(price_widget3.number_input("Price3"))
    l[2].append(date_widget3.date_input("Date3"))
    l[2].append(from_widget3.number_input("From Hour3", min_value=0, max_value=23))
    l[2].append(to_widget3.number_input("To Hour3", min_value=0, max_value=23))

if(st.button("Confirm the Bids")):
    df=pd.read_csv(f"""Data/{get("user")}.csv""")

    if (Bid_Input == "Single Bid"):
        l=[l[0]]

    p=True  ## if everything is correct
    for j in range (len(l)):
        for i in range (l[j][3], l[j][4]):
            if(len(df[(df['date']==l[j][2].day) & (df['hour']==i) & (df['month']==l[j][2].month)])==0):
                p=False
                st.error("Please recheck the bids")
                break
    if(p):
        st.success("Bids Submitted")
        for j in  range (len(l)):
            for i in range (l[j][3],(l[j][4]+1)):
                Obj={"User": get("user"),
                     "Quantity": l[j][0],
                     "Price": l[j][1],
                     "Date":l[j][2].day,
                     "Month": l[j][2].month,
                     "Year": l[j][2].year,
                     "Hour": i,
                     "State": "Waiting"}
                storethedata("Bids",Obj)












