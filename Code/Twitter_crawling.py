
twitter_consumer_key = "hHPuNLAkNrUiThoFrkCklirWQ"
twitter_consumer_secret = "b8EXmznl9R76uMPZHBAox5k34MemelY86NbSVvInbKPT9InmqD"  
twitter_access_token = "2665614932-9Yagdy0pMV8bL4o02S9I0tIMvup42PjmwRwwAqg"
twitter_access_secret = "T9y5QiMc1f9BjNvzogOYzZCIwUC0gCTl6FyCH9qVald6l"


# twitter module ###############################################################
import twitter
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

query = "서울핫플"
statuses = twitter_api.GetSearch(term=query, count=1)
for status in statuses:
    print(status.text)

    
    
from collections import Counter
query = "서울핫플"
statuses = twitter_api.GetSearch(term=query, count=100)
result = []
for status in statuses:
    for tag in status.hashtags:
        result.append(tag.text)
        
Counter(result).most_common(20)



import json, os
query = ["서울핫플"]
os.chdir(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\Instagram_Crawler\crawled_data\twitter')
output_file_name = "stream_result.txt"
with open(output_file_name, "w", encoding="utf-8") as output_file:
    stream = twitter_api.GetStreamFilter(track=query)
    while True:
        for tweets in stream:
            tweet = json.dumps(tweets, ensure_ascii=False)
            print(tweet, file=output_file, flush=True)
            
###############################################################################

    

# tweepy module ###############################################################
import tweepy
import pandas as pd

## 트위터 api와 연결
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

print(api) # 객체 생성되면 연결 성공

keyword = '서울핫플'
tweet_list = []
korea_geo = "%s,%s,%s" % ("35.95", "128.25", "1000km")

for status in tweepy.Cursor(api.search_tweets, q=keyword, geocode=korea_geo).items(500):
    temp_list = [status.text, status.created_at, status.retweet_count, status.favorite_count]
           
    try:
        temp_list.append(status.retweeted_status.text)
    except:
        temp_list.append('Not Retweeted')
            
    temp_list.extend([status.user.name, status.user.followers_count])
                
    tweet_list.append(temp_list)

df = pd.DataFrame(tweet_list, columns=['Text', 'Created_Date', '#_of_Retweets', '#_of_Likes', 'Original_Text', 'User', 'User_#_of_Followers'])
df.head()



###############################################################################