import firebase_test
from firebase_test import credentials
from firebase_test import db
cred = credentials.Certificate("secret.json")
firebase_admin.initialize_app(cred,
    {'databaseURL': 'https://test-305e4-default-rtdb.firebaseio.com/'}

)




# Import database module.


# Get a database reference to our posts
ref = db.reference('https://test-305e4-default-rtdb.firebaseio.com/')
ref.update({"hi":1234})

# Read the data at the posts reference (this is a blocking operation)
ref = db.reference('key')
print(ref.get())