
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

login_page=st.Page(
    page="Pages/login.py",
    title="Login",
    icon="👤",
    default=True
)
register_page=st.Page(
    page="Pages/register.py",
    title="Register",
    icon="📊"
)
bidding_page = st.Page(
    page="Pages/bidding.py",
    title="Make your bids",
    icon="💸"  # Money with wings, indicating bids or money transactions
)

check_dates = st.Page(
    page="Pages/check_dates.py",
    title="Check the Bidding hours",
    icon="⏰"  # Alarm clock, indicating time for checking bidding hours
)

result_page = st.Page(
    page="Pages/result.py",
    title="Result Window",
    icon="🏆"  # Trophy, indicating results or success
)

logout=st.Page(
    page="Pages/logout.py",
    title="Logout"
)



admin1_page=st.Page(
    page="Pages/admin1.py",
    title="Make Decision"
)

admin2_page=st.Page(
    page="Pages/admin2.py",
    title="Show Result"
)


## -- Navigation setup -- ##

if("user" in st.session_state and st.session_state["user"]=="admin"):
    pg=st.navigation({
        "Dashboard": [admin1_page,admin2_page,logout]
    })

elif("user" in st.session_state):
    pg=st.navigation({
        "Dashboard": [bidding_page,check_dates,result_page,logout]
    })

else:
    pg=st.navigation({
        "Users":[login_page,register_page]
    })

pg.run()




