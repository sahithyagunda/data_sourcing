import requests
import pandas as pd


## sends a get request to the fake user data api and fetches 50 random users
response = requests.get("https://randomuser.me/api/?results=50")

## converts the response to json format
data = response.json()


## extracts the list of users from the json data
users = data['results']

rows = []

for user in users:
    rows.append({
        'name': f"{user['name']['first']} {user['name']['last']}",
        'gender':user['gender'],
        'email':user['email'],
        'city':user['location']['country'],
        'username':user['login']['username'],
    })


## creates a pandas dataframe from the list of user dictionaries

df = pd.DataFrame(rows)

print(df)

df.to_csv('fake_user_data.csv',index=False)