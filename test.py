__author__ = 'sn'
import praw
r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
r.set_oauth_app_info(
    client_id='GTlkDtvm2KkPjA',
    client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
    redirect_uri='http://127.0.0.1:5000/')
r.login(username="bad_guy_1991", password="qweasd")

link = "http://arstechnica.com/business/2014/11/how-you-yes-you-can-get-around-ubers-surge-pricing/"
print "type: ", type(link)
for item in r.search(link):
    print item
