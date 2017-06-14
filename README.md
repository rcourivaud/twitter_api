# twitter_api

## Installation 

```bazaar
pip install git+
```

## Usage

```bazaar

    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"

    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    
    
    twa = TwitterAPI(consumer_key=consumer_key,
                     consumer_secret=consumer_secret,
                     access_token=access_token,
                     access_token_secret=access_token_secret)
                     
    pritn(twa.get_user_data())
    
```