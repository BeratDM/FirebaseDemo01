#Firebase - backend as a service
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Fetch the service account key JSON file contents
#The .json file is located in the same path with this file but not published
cred = credentials.Certificate("testproject01-serviceAccountKey.json")

#Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://testproject01-aa1b0-default-rtdb.europe-west1.firebasedatabase.app/'
})

#Save data
ref = db.reference('py/')
users_ref = ref.child('users')
users_ref.set({
    'beratu': {
        'date_of_birth': 'Jan 3, 1825',
        'full_name': 'Berat U'
    },
    'maxi': {
        'date_of_birth': 'Jan 1, 1349',
        'full_name': 'Max I'
    }
})

#Update data
hopper_ref = users_ref.child('maxi')
hopper_ref.update({
    'nickname': 'MAXIMUS',
    'full_name': 'Max INX'
})

#Get data reference
handle = db.reference('py/users/maxi')

#Read the data at the reference(this is a blocking operation)
print(ref.get())
#print(handle.get())