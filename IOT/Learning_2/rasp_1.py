# checking for Internet Connection
import urllib.request
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import datetime


def check_wifi_is_connected():
    try:
        # request intenet to find the url and return its data
        print(urllib.request.urlopen('http://google.com'))
        return True
    except:
        return False


# check wifi is connected or not
# return :  True:- connected
#           False :- Not Connected
# check_wifi_is_connected()


# initialize cloud fire store
# Connect Pi to firebase using credentials
# which is json file :- credentials.json
# it return firestore client object
def connect_to_firebase():
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred)

    # initialize database connection
    db = firestore.client()
    # print(type(db))
    # <class 'google.cloud.firestore_v1.client.Client'>
    return db


db = connect_to_firebase()

#####
# Tocken for accesing the database
uid_token = u'VA85MuoofzZiR1LKm7CT30GngWs2'
#####


# testing     done
def read_data(db):
    user_ref = db.collection(u'VA85MuoofzZiR1LKm7CT30GngWs2')
    docs = user_ref.stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


# read_data(db)
#


# Synchronize the device condition with server at only one time
# On and off Motter according to Server Command.
# time interval to check motor is on or off = 5 minutes = 5 * 60 = 300 seconds.
# if time interval of motor in standard time interval then motor will on on
# else motor will be off
# if user forced to off motor then server last time will be off

def check_motor_state(db):
    motor_ref = db.collection(uid_token).document(u"Controller")
    motor_Data = motor_ref.get()
    if motor_Data.exists:
        print("motor data : {}".format(motor_Data.to_dict()))

    # motor last means current statues
    motor_last_statues = motor_Data.to_dict().get(u"Status")
    print(motor_last_statues)

    # motor last On time
    motor_lastOn_time = motor_Data.to_dict().get(u"LastOn")
    # convert google datetime object into python datetime object
    motor_lastOn_time_datetime = datetime.datetime.combine(date=motor_lastOn_time.date(
    ), time=motor_lastOn_time.time(), tzinfo=motor_lastOn_time.tzinfo)

    # motor till on time
    motor_Ontill_time = motor_Data.to_dict().get(u"OnTill")
    # convert google datetime object into python datetime object
    motor_Ontill_time_datetime = datetime.datetime.combine(date=motor_Ontill_time.date(
    ), time=motor_Ontill_time.time(), tzinfo=motor_Ontill_time.tzinfo)

    # getting current time from firebase Server
    current_datetime = datetime.datetime.utcnow()
    current_datetime = current_datetime.replace(tzinfo=datetime.timezone.utc)
    print(current_datetime.tzinfo)
    print(motor_lastOn_time_datetime.tzinfo)
    print(motor_Ontill_time_datetime.tzinfo)
    print(motor_lastOn_time_datetime)
    print(current_datetime)
    print(motor_Ontill_time_datetime)

    # if current_datetime in interval of Onmotor then
    # Onmotor pin on raspberry pi
    # update status on firebase
    if current_datetime < motor_Ontill_time_datetime and current_datetime > motor_lastOn_time_datetime:
        # motor pin on
        # ??????????????????????????

        # update status on firebase
        motor_ref.update(
            {u'Status': True}
        )


check_motor_state(db)
