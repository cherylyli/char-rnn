import os
import time
from markovbot import MarkovBot
from config import Config

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'input.txt')

tweetbot.read(book)
passwords = Config()

my_first_text = tweetbot.generate_text(25, seedword=['dream', 'America'])
print("tweetbot says: ")
print(my_first_text)

cons_key = passwords.cons_key
cons_secret = passwords.cons_secret
access_token = passwords.access_token
access_token_secret = passwords.access_token_secret

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

while True:
	targetString = "DonaldTrump"
	keywords = []

	prefix = None
	suffix = "#ObamaBot"
	maxconvdepth = 5


	tweetbot.twitter_autoreply_start(targetString, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
	tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=30, keywords=None, prefix=None, suffix=suffix)
 
 	time.sleep(100)
 	print("hello")
	# Use the following to stop auto-responding
	# (Don't do this directly after starting it, or your bot will do nothing!)
	tweetbot.twitter_autoreply_stop()