"""
what we implement here:

We get user info from API

Get preferences from MongoDB

Merge on username, so every user now has their prefs attached (if any)

how='left' ensures all API users stay, even if no prefs found

"""
import requests
import pandas as pd
from data_mongodb.connecting_mongodb import client

def fetch_api_users():
    url = "https://randomuser.me/api/?results=5"
    resp = requests.get(url)
    data = resp.json()
    users = []

    for user in data['results']:
        users.append({
            'username': user['login']['username'],
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'city': user['location']['city']
        })
    return pd.DataFrame(users)


def fetch_mongo_user_prefs():
    db = client['api_data']
    collection = db['fake_user_data']

    prefs = list(collection.find({}, {'_id': 0}))  # exclude _id
    return pd.DataFrame(prefs)


api_df = fetch_api_users()
mongo_df = fetch_mongo_user_prefs()

combined_df = pd.merge(api_df, mongo_df, on='username', how='left')
combined_df.to_csv('combined_user_data.csv', index=False)
