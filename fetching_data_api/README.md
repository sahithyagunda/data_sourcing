This project demonstrates how to fetch, clean, and store data from multiple public APIs using Python. The data includes:

Fake user profiles (randomuser.me)

Country information (restcountries.com)

Cryptocurrency prices (CoinGecko)

Weather data (OpenWeatherMap)


api_data_fetching

├── fake_user_data_fetch.py            # Fetches and stores fake user profiles

├── country_data_fetch.py              # Fetches global country data

├── crypto_data_fetch.py               # Fetches crypto prices from CoinGecko

├── weather_data_fetch.py              # Fetches weather data for a given city

├── fake_user_data.csv                # Output from fake_user_data_fetch

├── real_crypto_data.csv              # Output from crypto_data_fetch

└── README.md                          # You're reading it!

Dependencies

Install all required libraries using pip:

pip install pandas requests

1. fake_user_data_fetch.py

Source: randomuser.me

What it does: Fetches 50 fake users and stores them in fake_user_data.csv

Data Fields:

Name

Gender

Email

Country (used as City)

Username

CSV Output: fake_user_data.csv

2. country_data_fetch.py

Source: restcountries.com

What it does: Fetches info for all countries and stores in a DataFrame

Data Fields:

Country Name

Capital

Region

Population

Languages

Currencies

Flag URL

You can extend this by saving it as a CSV (e.g. country_data.csv).

3. crypto_data_fetch.py

Source: CoinGecko

What it does: Fetches current prices of selected cryptocurrencies

Coins: Bitcoin, Ethereum, Ripple, Litecoin, Cardano

Currencies: USD, INR, EUR, GBP

CSV Output: real_crypto_data.csv

4. weather_data_fetch.py

Source: OpenWeatherMap

What it does: Fetches real-time weather data for a given city

Note: Requires a valid API key.

Example city: Delhi

Replace API_KEY in the script with your OpenWeatherMap API key.
