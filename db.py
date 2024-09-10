import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('deleteme-367bd-firebase-adminsdk-x424d-dd97c64bc9.json')
app = firebase_admin.initialize_app(cred)

def storethedata(Obj1):
# Use a service account.

    db = firestore.client()
    data=[Obj1]
    print(data)
    #
    for record in data:
        doc_ref=db.collection(u"Users").document(record["User"])
        doc_ref.set(record)


def checkdata(Obj1):


    db = firestore.client()

    users_ref = db.collection(u"Users")
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
        if(doc.id==Obj1[0] and doc.to_dict()["Password"]==Obj1[1]):
            print("Login successfully")
            return True

    print("Fail")

    return False