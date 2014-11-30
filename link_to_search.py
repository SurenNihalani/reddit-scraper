__author__ = 'sn'

import praw
import json
import smtplib
from smtplib import SMTPException
import traceback
import sys
import exceptions


def send_email(exception):
    print "exception: ", str(exception)
    sender = 'from@fromdomain.com'
    receivers = ['suren.k.n@icloud.com', 'khare.ashwini@gmail.com']

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
    if isinstance(t, str):
        return t
    return ','.join([str(x) for x in t]) + '\n'


index_to_start = 0
records_to_skip = 0
records_done = 0

with open('data2.csv', 'a') as x:
    with open('links.csv', 'r') as f:
        r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
        r.set_oauth_app_info(
            client_id='GTlkDtvm2KkPjA',
            client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
            redirect_uri='http://127.0.0.1:5000/')
        r.login(username="bad_guy_1991", password="qweasd")

        for line in f:
            try:
                index_to_start += 1
                if index_to_start <= records_to_skip:
                    continue

                line = line.strip()
                line = line.split()
                if len(line) != 5:
                    print "MESSED UP LIN: ", line
                    continue
                link, author, subreddit, time, score = line

                all_items = []
                for item in r.search(link):
                    if item.is_self:
                        continue
                    url = item.url
                    user = item.author.name
                    time = item.created
                    score = item.score
                    subrreddit = item.subreddit
                    all_items.append((user, subreddit, time, score))
                x.write(tuple_to_string((index_to_start, link, author, subreddit, time, score, json.dumps(all_items))))
                records_done += 1
                if records_done % 100 == 0:
                    x.flush()
                    print "records done: ", records_done

            except exceptions.AttributeError as e:
                print link
                print e
                print index_to_start
                pass
            except:
                exception = ''.join(traceback.format_tb(sys.exc_info()[2])) + '\n' + str(
                    sys.exc_info()[0]) + '\n line: ' + str(index_to_start)
                exception = tuple_to_string(exception)
                exception = exception + ' ' + '\n' + str(sys.exc_info()[1])
                send_email(exception)
                print "records done: ", records_done
                print exception
                print str(sys.exc_info()[0])
                print str(sys.exc_info()[1])

