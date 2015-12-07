import tweepy, random
#from sense_hat import sense_hat

#sense = SenseHat()

# Twitter OAuth
CONSUMER_KEY = 'kSIetSbnmhIkLcYsV3ID02MNe'
CONSUMER_SECRET = 'v2pYe59qnRgqzr6ERWkjFDueJWNld1tp1YZgCq3QFEyV9Rmbbp'
ACCESS_KEY = '4406464606-N9YmeHiNCHoCtrMJx3LrY2eIvFk9bydWBs51MDw'
ACCESS_SECRET = 'iAlbyjm3VIYnVGrKOCfrpG8NIadK00C363d117LQYc6nW'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# tweet options
normal_tweets = ['It\'s a beautiful day today!', 'Feelin\' great!!', 'Happy and healthy!']
cold_tweets = ['Brrrrrrrr!!', 'It\'s getting kinda chilly in here']
hot_tweets = ['Whew! It\'s hot in here', 'I\'m burnin\' up in here!!']
dark_tweets = ['Can someone turn on the lights?', 'I\'m afraid of the dark...']
bright_tweets = ['Wow it\'s way too bright out', 'Ah! I need a pair of sunglasses!', '']
dry_tweets = ['I\'m PARCHED!', 'It\'s important to hydrate!', 'Don\'t forget to water me today!']
wet_tweets = ['No more water please!', 'I am DRENCHED!']

# threshold values for temp, light, humidity
temp_vals = { min: 70.0, max: 80.0 }
light_vals = { min: 10.0, max: 20.0 }
humidity_vals = { min: 15.0, max: 30.0 }

def generate_tweet(temp, light, humidity):
    # temp checking
    if(temp < temp_vals[min]):
        send(random.choice(cold_tweets))
    elif(temp > temp_vals[max]):
        send(random.choice(hot_tweets))
    # light checking
    elif(light < light_vals[min]):
        send(random.choice(dark_tweets))
    elif(light > light_vals[max]):
        send(random.choice(bright_tweets))
    # humidity checking
    elif(humidity < humidity_vals[min]):
        send(random.choice(dry_tweets))
    elif(humidity > humidity_vals[max]):
        send(random.choice(wet_tweets))
    # if everything is good
    else:
        send(random.choice(normal_tweets))

def send(tweet):
    api.update_status(tweet)

# placeholder function for light values
def get_light():
    return random.uniform(0.0, 30.0)

def main():
    #t = sense.get_temperature()
    l = get_light()
    #h = sense.get_humidity()
    #generate_tweet(t, l, h)


#main()
api.update_with_media('pvz.gif', status="Plants!!!")
