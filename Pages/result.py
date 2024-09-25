import streamlit as st
from Pages.globals import insert,get
from db import checkbids
st.title("Result")

from_date_widget, to_date_widget=st.columns([1,1])
from_date=from_date_widget.date_input("From Date")
to_date=to_date_widget.date_input("To Date")
state=st.radio("Which Bids to show??" ,["Selected","Non Selected", "Waiting"])

usr=get("user")
Obj1=[usr, from_date,to_date, state]

df=checkbids(Obj1)

st.table(df)





