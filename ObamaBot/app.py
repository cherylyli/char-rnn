import os
import time
from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'input.txt')

tweetbot.read(book)

my_first_text = tweetbot.generate_text(25, seedword=['dream', 'America'])
print("tweetbot says: ")
print(my_first_text)

cons_key = "npSslr2RA4y9qezk8jRVjJTPF"
cons_secret = "FBofbsP78nHJ5KJB0Gyk8Ni7jcCj7t8YJM78wsIXJNxIZ3XoFk"
access_token = "1580605578-19qlEeAvQyeY1GEr43F09fPg8UBkjSltjhbZ21e"
access_token_secret = "xUsHipH2OJ1A3o90vH4uD1D2xGU3s2KC9PRDiMhmwGjVa"

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

while True:
	targetString = "DonaldTrump"
	keywords = []

	prefix = '@realDonaldTrump'
	suffix = "#ObamaBot"
	maxconvdepth = 5


	tweetbot.twitter_autoreply_start(targetString, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
 
 	time.sleep(100)
 	print("hello")
	# Use the following to stop auto-responding
	# (Don't do this directly after starting it, or your bot will do nothing!)
	tweetbot.twitter_autoreply_stop()