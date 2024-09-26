import streamlit as st
from db import checkbids
## Convention - [User,From Date,To Date State]

st.title("Show the Result")
from_date_widget, to_date_widget=st.columns([1,1])
from_date=from_date_widget.date_input("From Date")
to_date=to_date_widget.date_input("To Date")
state=st.radio("Which type of bids you want to see?",["Selected","Non Selected","Waiting"])

Obj1=["",from_date, to_date, state]
st.table(checkbids(Obj1)[0])
