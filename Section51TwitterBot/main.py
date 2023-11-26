from speed_twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 10000
PROMISED_UP = 100000

speed_twitter_bot = InternetSpeedTwitterBot()

speed_twitter_bot.get_internet_speed()

if speed_twitter_bot.up < PROMISED_UP or speed_twitter_bot.down < PROMISED_DOWN:
    text_to_tweet = f"Hey Internet Service Provider! Why is my internet speed {speed_twitter_bot.up} UP / {speed_twitter_bot.down} DOWN when I pay for {PROMISED_UP} UP and {PROMISED_DOWN} DOWN?"
    speed_twitter_bot.tweet_at_provider(text_to_tweet=text_to_tweet)

