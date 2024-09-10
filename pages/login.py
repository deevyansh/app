import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from db import checkdata

st.title("Login")
usr=st.text_input("Username")
password=st.text_input("Password")


if(st.button("Login")):
    Obj1=[usr,password]
    if(checkdata(Obj1)):
        st.success('Login Successfully!', icon="✅")
        st.balloons()
    else:
        st.error('Error in Login', icon="🚨")