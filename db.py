import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
from datetime import datetime

cred = credentials.Certificate('deleteme-367bd-firebase-adminsdk-x424d-dd97c64bc9.json')
app = firebase_admin.initialize_app(cred)

def storethedata(collection,Obj1):
# Use a service account.

    db = firestore.client()
    data=[Obj1]
    #
    for record in data:
        db.collection(f"{collection}").add(record)

def checkdata(collection,Obj1):
    db = firestore.client()
    users_ref = db.collection(f"{collection}")
    docs = users_ref.stream()
    for doc in docs:
        if(doc.to_dict()["User"]==Obj1[0] and doc.to_dict()["Password"]==Obj1[1]):
            print("Login successfully")
            return True
    return False


def checkbids(Obj1):
    ## Convention - [User,From Date,To Date State]
    db=firestore.client()
    bids_ref=db.collection("Bids")
    docs=bids_ref.stream()
    df=pd.DataFrame()
    list=[]
    for doc in docs:
        date=datetime(doc.to_dict()["Year"], doc.to_dict()["Month"], doc.to_dict()["Date"]).date()
        if((doc.to_dict()["User"]==Obj1[0] or Obj1[0]=="") and doc.to_dict()["State"]==Obj1[3] and date>=Obj1[1] and date<=Obj1[2]):
            df_dict=pd.DataFrame([doc.to_dict()])
            df=pd.concat([df,df_dict], ignore_index=True)
            list.append(doc.id)
    return df,list

def changebids(Obj1, doc_id):
    db=firestore.client()
    if(Obj1["Finalized Quantities"]==0):
        db.collection("Bids").document(doc_id).update({"State": "Non Selected"})
    else:
        db.collection("Bids").document(doc_id).update({"State":"Selected", "Quantity_Selected":Obj1["Finalized Quantities"]})
    return True

def return_email(Obj1):
    db=firestore.client()
    users_ref=db.collection("Users")
    docs=users_ref.stream()
    for doc in docs:
        if(doc.to_dict()["User"]==Obj1["User"]):
            return doc.to_dict()["Email"]
