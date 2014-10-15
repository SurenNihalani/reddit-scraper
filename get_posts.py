
import praw
import pprint
import signal
import time
import MySQLdb as db
import smtplib
from smtplib import SMTPException
import requests
import sys

r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
r.set_oauth_app_info(
    client_id='GTlkDtvm2KkPjA',
    client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
    redirect_uri='http://127.0.0.1:5000/')
r.login(username="bad_guy_1991", password="qweasd")


users = ['TerenceCardinal']

freq = {}

for u in users:
    user = r.get_redditor(u)
    if user in freq:
        continue
    c = 0
    for lol in user.get_submitted():
        c += 1
    freq[u] = c


print freq.values()
