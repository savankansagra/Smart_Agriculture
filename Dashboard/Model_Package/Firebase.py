import pyrebase
from getpass import getpass
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


firebaseConfig = {
    "apiKey": "AIzaSyAtT0_MT2_REFiOHQriadyDrt0yS8j8cuM",
    "authDomain": "farmerautomode.firebaseapp.com",
    "databaseURL": "https://farmerautomode.firebaseio.com",
    "projectId": "farmerautomode",
    "storageBucket": "farmerautomode.appspot.com",
    "messagingSenderId": "15358417331",
    "appId": "1:15358417331:web:8d0f53065ff57d13ac13c6",
    "measurementId": "G-CHDV44E9L0"
}

firebase = pyrebase.initialize_app(firebaseConfig)

cred = credentials.Certificate(r"D:\study\sem-8\project\Git-Ex-2\Smart_Agriculture\Dashboard\Model_Package\firebase_cred.json")
firebase_admin.initialize_app(cred)

def getAuth(email,password):
    auth1 = False
    auth = firebase.auth()

    try:
        login = auth.sign_in_with_email_and_password(email, password)
        login = auth.refresh(login['refreshToken'])
        uid = login['userId']
        auth1 = True
    except requests.exceptions.HTTPError as e:
        auth1 = False
        uid = ''

    return auth1,uid

def getData(uid):
    db = firestore.client()
    users_ref = db.collection(uid)
    docs = users_ref.stream()
    data = {}
    for doc in docs:
        data[doc.id] =  doc.to_dict()

    return data

def updateData(uid,data):
    db = firestore.client()
    doc_ref = db.collection(uid).document(u'Controller')
    doc_ref.set(data)
