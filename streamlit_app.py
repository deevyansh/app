
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

login_page=st.Page(
    page="pages/login.py",
    title="Login",
    icon="👤",
    default=True
)
register_page=st.Page(
    page="pages/register.py",
    title="Register",
    icon="📊"
)



## -- Navigation setup -- ##
pg=st.navigation({
        "Account": [login_page,register_page]
        })
pg.run()

