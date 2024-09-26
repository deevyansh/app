import streamlit as st
from db import checkbids, changebids
import pandas as pd
## Convention - [User,From Date,To Date State]
st.title("Make Decision Window")
from Pages.marketalgo import economic
#(PD,PD_min,PD_max,c)


st.write("Please enter the Date, Hour and Demand to see the Results")
date_input_widget,hour_widget=st.columns([1,1])
date=date_input_widget.date_input("Date")
hour=hour_widget.number_input("Hour", min_value=0, max_value=23)
demand=st.number_input("Power Demand in KWh")



if (st.button("Show the Result")  or ("df" in st.session_state)):
    Obj1 = ["", date, date, "Waiting"]

    result = checkbids(Obj1)
    df = result[0]
    doc_id_list = result[1]
    df = df.loc[df['Hour'] == hour]
    doc_id_list = [doc_id_list[i] for i in df.index]

    print(df)
    if len(df)>0:
        PD_min=[0 for i in range (len(df))]
        c=df["Price"].tolist()
        PD_max=df["Quantity"].tolist()
        PD=demand
        if((economic(PD,PD_min,PD_max,c))is not None):
            df["Finalized Quantities"]=economic(PD,PD_min,PD_max,c)
            df=df.reset_index(drop=True)
            st.table(df)
            st.success("Result Generated")
            st.balloons()
        else:
            st.error("Not enough Bids. Lower the Demand")
        st.session_state["df"]=df
        st.session_state["doc_id_list"]=doc_id_list
        if(st.button("Finalize the Result")):
            print("Hello i am here now")
            df=st.session_state["df"]
            for i in range (len(df)):
                Obj1=df.loc[i]
                changebids(Obj1.to_dict(), doc_id_list[i])
            del st.session_state["doc_id_list"]
            del st.session_state["df"]
            st.success("Result Finalized!!!")
    else:
        st.error("No bids for that particular hour")






