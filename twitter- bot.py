import tweepy
def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret =  os.getenv('consumer_secret')
  access_token =   os.getenv('access_token')
  access_token_secret =   os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)
 # api.verify_credentials()
  print('API Created')
  return api

import time
def follower(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers


api = create_api()

while True:
    user = api.get_user('@kushi59561143')
    api.update_profile(name=f'KUSHI|{follower(user)} Followers')
    print(f'Updating Twitter Name : KUSHI|{follower(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
          
    
           
           
  
