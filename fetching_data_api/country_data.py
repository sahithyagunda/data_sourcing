import requests
import pandas as pd


url = "https://restcountries.com/v3.1/name/all"

response = requests.get(url)
data = response.json()

country_list = []
for country in data:
    country_list.append({
        "name": country["name"]["common"],
        "capital": country.get("capital", ["N/A"])[0],
        "region": country.get("region", "N/A"),
        "population": country.get("population", 0),
        "languages": ", ".join(country.get("languages", {}).values()),
        "currencies": ", ".join([v["name"] for v in country.get("currencies", {}).values()]),
        "flag_url": country.get("flags", {}).get("png", "")
    })

df = pd.DataFrame(country_list)
print(df.head())
print("Total countries:", len(df))