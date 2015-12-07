# The Tweeting Garden

## What makes your garden grow?
Plants need lot's of things to keep them alive - light, water and carbon dioxide being the most important.
Plants also need a nice environment. They don't like being too hot or too cold for instance.

In this project, you're going to use a Raspberry Pi and a whole bunch of sensors to let the plants in your garden tweet you, when they need water, light or a change in temperature.

## Coding your garden
Some of the code has been written for you, and some you are going to need to code yourself.

Open up `tweet-garden.py` in IDLE to get started.


## Lists of tweets
Scroll to the `#tweet options` section

The first set of tweets has been done for you.

```python
# tweet options
normal_tweets = ["It's a beautiful day today!", "Feelin' great!!", "Happy and healthy!"]
```

This is called a `list`. Lists in Python are surrounded by `[ ]`. Items in a list are seperated by a comma (`,`). You can makes lists of anything you like, and in this case a list of tweets has been made.

You need to create some lists of your own now. The names of the lists are shown below, and you should fill them with tweets.

```python
cold_tweets
hot_tweets
dark_tweets
bright_tweets
dry_tweets
wet_tweets
```

## Extreme Dictionaries

Scroll down to the `# threshold values for temp, light, humidity` section.

The first set of ranges has been done for you

```python
# threshold values for temp, light, humidity
temp_vals = { min: 70.0, max: 80.0 }
```

This is called a dictionary. In this case you have a dictionary of temperature values (`temp_vals`). A dictionary consists of lots of `keys` and `values`. In this case they keys are `min` and `max` which are short for *minimum* and *maximum*. The values are the maximum and minimum temperatures.

Dictionaries are surrounded by `{ }` and there are always colons (`:`) between the `keys` and `values`

You need to create your own dictionaries for light and humidity readings. The names are given to you below.

```python
light_vals
humidity_vals
```

## The thinking part

Lastly, you need to get your plant tweeting when it starts to feel uncomfortable. To do this you can use a technique called *conditional selection*

Scroll down to the section that says `def generate_tweet(temp, light, humidity):`
This is the start of a function definition. All the code inside needs to begin with 4 spaces (but your IDE should deal with that part for you.

Place your cursor on the end of the line that say `# temp checking` and press Enter.

Now you need to write code to tell if the temperature is between the max and min from the dictionary you made earlier.

You can start with this line:

```python
    if(temp < temp_vals[min]):
```

This is checking if the temperature is less than the min value in your dictionary.
If it is then you want to send a random cold_tweet.

```python
        send(random.choice(cold_tweets))
```

So the function should look like this now:

```python
def generate_tweet(temp, light, humidity):
    # temp checking
    if(temp < temp_vals[min]):
        send(random.choice(cold_tweets))
    # light checking
   	# humidity checking
	# if everything is good

```
Now you need to check if the temperature is above the maximum.

```python
    elif(temp > temp_vals[max]):
        send(random.choice(hot_tweets))
```

See if you can complete the function, too handle humidity and light as well.
