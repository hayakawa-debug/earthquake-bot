import feedparser
import tweepy
import os

# GitHub Secrets や環境変数から読み込む
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# OAuth1で認証
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# 気象庁公式の地震情報フィード
url = "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"
feed = feedparser.parse(url)

# 最新の地震情報を取得
if feed.entries:
    entry = feed.entries[0]
    title = entry.title
    link = entry.link

    # ツイート内容
    tweet = f"【気象庁 地震情報】\n{title}\n{link}"
    
    # ツイートを投稿
    try:
        api.update_status(tweet)
        print("✅ ツイート成功！")
    except tweepy.TweepyException as e:
        print("❌ ツイート失敗:", e)
else:
    print("❌ 地震情報が取得できませんでした。")
