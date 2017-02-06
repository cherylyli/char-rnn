import os
import time
import indicoio
from markovbot import MarkovBot
from config import Config
from random import randint

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
indicoio.config.api_key = passwords.indico_key
tweets = ["The judge opens up our country to potential terrorists and others that do not have our best interests at heart. Bad people are very happy!", "Interview with @oreillyfactor on Fox Network - 4:00 P.M. (prior to Super Bowl). Enjoy!", "Why aren't the lawyers looking at and using the Federal Court decision in Boston, which is at conflict with ridiculous lift ban decision?", "Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision", "What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?", "After being forced to apologize for its bad and inaccurate coverage of me after winning the election, the FAKE NEWS nytimes is still lost!", "The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned!", "Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it's death and destruction!", "When a country is no longer able to say who can, and who cannot , come in and out, especially for reasons of safety and .security  big trouble!", "Countries charge U.S. companies taxes or tariffs while the U.S. charges them nothing or little.We should charge them SAME as they charge us!", "We must keep 'evil' out of our country!", "A new radical Islamic terrorist has just attacked in Louvre Museum in Paris. Tourists were locked down. France on edge again. GET SMART U.S.",  "Professional anarchists, thugs and paid protesters are proving the point of the millions of people who voted to MAKE AMERICA GREAT AGAIN!", "Meeting with biggest business leaders this morning. Good jobs are coming back to U.S., health care and tax bills are being crafted NOW!", "Thank you to Prime Minister of Australia for telling the truth about our very civil conversation that FAKE NEWS media lied about. Very nice!", "Iran is playing with fire - they don't appreciate how 'kind' President Obama was to them. Not me!", "Yes, Arnold Schwarzenegger did a really bad job as Governor of California and even worse on the Apprentice...but at least he tried hard!", "Iran was on its last legs and ready to collapse until the U.S. came along and gave it a life-line in the form of the Iran Deal: $150 billion", "Iran has been formally PUT ON NOTICE for firing a ballistic missile.Should have been thankful for the terrible deal the U.S. made with them!", "Attending Chief Ryan Owens' Dignified Transfer yesterday with my daughter Ivanka was my great honor. To a great and brave man - thank you!", "Congratulations to Rex Tillerson on being sworn in as our new Secretary of State. He will be a star!", "If U.C. Berkeley does not allow free speech and practices violence on innocent people with a different point of view - NO FEDERAL FUNDS?", "Do you believe it? The Obama Administration agreed to take thousands of illegal immigrants from Australia. Why? I will study this dumb deal!", "Iran is rapidly taking over more and more of Iraq even after the U.S. has squandered three trillion dollars there. Obvious long ago!"]


def get_rand_tweet(tweets):
	"""get a random tweet from the list of tweets given and return it"""
	return tweets[randint(0, len(tweets)-1)]



while True:
	targetString = "DonaldTrump"


	analyze_tweet = get_rand_tweet(tweets)
	print("analyzing tweet: " + analyze_tweet)
	unfilter_keywords = indicoio.keywords(analyze_tweet, version=2)
	keywords = [keyword for keyword, value in unfilter_keywords.iteritems() if value > 0.2]
	print(keywords)

	targetString = "pseudoObamaBot"
	prefix = None
	suffix = "#ObamaBot"
	maxconvdepth = 8
	kywds = []


	tweetbot.twitter_autoreply_start(targetString, keywords=kywds, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
	tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=10, keywords=keywords, prefix=None, suffix=suffix)
 

 	time.sleep(600)
 



	# Use the following to stop auto-responding
	# (Don't do this directly after starting it, or your bot will do nothing!)
	tweetbot.twitter_autoreply_stop()
	time.sleep(60)
