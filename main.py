
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
    title="Submit the bids",
    icon="💸"  # Money with wings, indicating bids or money transactions
)

check_dates = st.Page(
    page="Pages/check_dates.py",
    title="Available Flexible Hours",
    icon="⏰"  # Alarm clock, indicating time for checking bidding hours
)

result_page = st.Page(
    page="Pages/result.py",
    title="Display Result",
    icon="🏆"  # Trophy, indicating results or success
)

logout=st.Page(
    page="Pages/logout.py",
    title="Logout"
)



admin1_page=st.Page(
    page="Pages/admin1.py",
    title="Market Clearance Window"
)

admin2_page=st.Page(
    page="Pages/admin2.py",
    title="Available Bids"
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
st.sidebar.image("Screenshot 2024-09-30 at 9.26.48 PM.png")
st.sidebar.write("Please send your queries at flexiblemarket0@gmail.com by your registered email id.")
pg.run()



