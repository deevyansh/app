
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
bidding_page = st.Page(
    page="pages/bidding.py",
    title="Make your bids",
    icon="💸"  # Money with wings, indicating bids or money transactions
)

check_dates = st.Page(
    page="pages/check_dates.py",
    title="Check the Bidding hours",
    icon="⏰"  # Alarm clock, indicating time for checking bidding hours
)

result_page = st.Page(
    page="pages/result.py",
    title="Result Window",
    icon="🏆"  # Trophy, indicating results or success
)

logout=st.Page(
    page="pages/logout.py",
    title="Logout"
)


## -- Navigation setup -- ##

if("user" in st.session_state):
    pg=st.navigation({
        "Dashboard": [bidding_page,check_dates,result_page,logout]
    })
else:
    pg=st.navigation({
        "Users":[login_page,register_page]
    })

pg.run()




