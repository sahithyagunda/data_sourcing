import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    'ids': 'bitcoin,ethereum,ripple,litecoin,cardano',
    'vs_currencies': 'usd,inr,eur,gbp'
}

response = requests.get(url,params=params)

data = response.json()

print(data) ## {'bitcoin': {'usd': 111264, 'inr': 9789691, 'eur': 94831, 'gbp': 82321} -- nested dictionary

## flatten the nested dictionary
flat_data = []
for coin,prices in data.items():
    for currency,price in prices.items():
        flat_data.append({''
        'coin':coin,
        'currency':currency,
        'price':price
        })

df = pd.DataFrame(flat_data)

print(df)

df.to_csv('real_crypto_data.csv',index=False)
