from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

# use a servie account
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# add data to document and collection
# first time the document and collection will created automatically
# collection :- Farmer
# Document :- First_Farmer

doc_ref = db.collection(u'Farmer').document(u'first_farmer')
doc_ref.set({
    u'farmer_name': u'savan kansagra',
    u'city': u'Amreli',
})

# create another document to send data in same collection
doc_ref = db.collection(u'Farmer').document(u'City_Parameter')
doc_ref.set({
    'Min_temp': '32.00000000005',
    'Max_temp': '42.10',
    'Average_temp': '37.02'
})

# we retrive the collected data from firestore
user_ref = db.collection('Farmer')
docs = user_ref.stream()

for doc in docs:
    print("{} => {}".format(doc.id, doc.to_dict()))


# Output
# """City_Parameter => {'Min_temp': '32.00000000005', 'Max_temp': '42.10', 'Average_temp': '37.02'}
# first_farmer => {'farmer_name': 'savan kansagra', 'city': 'Amreli'}"""
