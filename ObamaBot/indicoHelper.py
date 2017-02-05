import indicoio
from config import Config
from tweet import Tweet

class IndicoData:
	def __init__(self):
		passwords = Config()
		self.api_key = passwords.indico_key


	def getkeywords(self):
		indicoio.config.api_key = self.api_key

		keywords = indicoio.keywords("The judge opens up our country to potential terrorists and others that do not have our best interests at heart. Bad people are very happy!", version=2)

		filtered_keywords = [keyword for keyword, value in keywords.iteritems() if value > 0.3]

		print(keywords)
		print(filtered_keywords)
		return filtered_keywords

