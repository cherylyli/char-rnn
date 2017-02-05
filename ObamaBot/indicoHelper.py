import indicoio
from config import Config
from tweet import Tweet

passwords = Config()
indicoio.config.api_key = passwords.indico_key

keywords = indicoio.keywords("The judge opens up our country to potential terrorists and others that do not have our best interests at heart. Bad people are very happy!", version=2)

filtered_keywords = [keyword for keyword, value in keywords.iteritems() if value > 0.3]

print(keywords)
print(filtered_keywords)

