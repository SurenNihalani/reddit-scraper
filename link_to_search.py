__author__ = 'sn'

import praw
import json
import smtplib
from smtplib import SMTPException
import traceback
import sys

def send_email(exception):
    print "exception: ", str(exception)
    sender = 'from@fromdomain.com'
    receivers = ['suren.k.n@icloud.com']

    message = """From: Social computing  <redditer@reddit>
To: Les Redditorians
Subject: error occured in the process


    """ + str(exception)

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
    except SMTPException:
        print "Error: unable to send email"

def tuple_to_string(t):
    return ','.join([str(x) for x in t]) + '\n'

index_to_start = 0
limit = 0
records_done = 0

try:
    with open('data.csv', 'a') as x:
        with open('links.csv', 'r') as f:
            r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
            r.set_oauth_app_info(
                client_id='GTlkDtvm2KkPjA',
                client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
                redirect_uri='http://127.0.0.1:5000/')
            r.login(username="bad_guy_1991", password="qweasd")

            for line in f:
                if index_to_start < limit:
                    continue
                index_to_start += 1

                line = line.strip()
                line = line.split()
                link, author, subreddit, time, score = line

                all_items = []

                for item in r.search('url:' + link):
                    if item.is_self:
                        continue
                    url = item.url
                    if url != link:
                        continue
                    user = item.author.name
                    time = item.created
                    score = item.score
                    subrreddit = item.subreddit
                    all_items.append((author, subreddit, time, score))
                x.write(tuple_to_string((link, author, subreddit, time, score, json.dumps(all_items))))

                records_done += 1
                if records_done % 100 == 0:
                    x.flush()
                    print "records done: ", records_done


except:
    exception = ''.join(traceback.format_tb(sys.exc_info()[2]))
    send_email(exception)
    print exception