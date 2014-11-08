__doc__ = """

A reddit bot that snapshots the hot page (upto 100 submissions) for 30 subreddits from a file

"""

import praw
import pprint
import signal
import time
import MySQLdb as db
import smtplib
from smtplib import SMTPException
import requests
import sys
import itertools
import traceback


pp = pprint.PrettyPrinter(indent=4)

keep_bot_on = True


def turn_bot_off_on_ctrl_c(signal, frame):
    """The bot runs an while True loop. Ctrl c breaks that loop so we can clean up gracefully"""
    global keep_bot_on
    keep_bot_on = False


def send_email(exception):
    print "exception: ", str(exception)
    sender = 'from@fromdomain.com'
    receivers = ['suren.k.n@icloud.com','khare.ashwini@gmail.com']

    message = """From: Social computing  <redditer@reddit>
To: Les Redditorians
Subject: error occured in the process


    """ + str(exception)

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
    except SMTPException:
        print "Error: unable to send email"


signal.signal(signal.SIGINT, turn_bot_off_on_ctrl_c)


def insert_post_into_db(
        cursor,
        url="",
        author="",
        score=0,
        created_time=0,
        subreddit_url=""):
    """Stores a hot post into the db for analysis later"""
    sql = '''
        INSERT INTO reddit_hot_posts(
            url,
            author, 
            subreddit_url,
            created_time,
            score
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s
        ) ON DUPLICATE KEY UPDATE
            score = VALUES(score)
    '''
    top = cursor.execute(
        sql,
        (url, author, subreddit_url, created_time, score, )
    )


def run_bot():
    """Runs the bot. Everything you need to know about the bot is in this function"""
    r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
    r.set_oauth_app_info(
        client_id='GTlkDtvm2KkPjA',
        client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
        redirect_uri='http://127.0.0.1:5000/')
    r.login(username="bad_guy_1991", password="qweasd")
    subreddits = [
        r.get_subreddit(subreddit_name=sub_reddit_name)
        for sub_reddit_name in read_subreddits_to_monitor()]

    last_time_bot_ran = time.time()

    con = db.connect(
        'localhost',
        'redditor',
        'qweasd',
        'reddit',
        charset='utf8')

    with con:
        cur = con.cursor()
        cur.execute('''
            DROP TABLE reddit_hot_posts;
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS reddit_hot_posts (
                url VARCHAR(2000),
                author VARCHAR(100),
                subreddit_url VARCHAR(1000),
                created_time BIGINT,
                score BIGINT,
                CONSTRAINT primary_key_post PRIMARY KEY (
                    url(30), 
                    author(10), 
                    subreddit_url(30)
                )
            );
        ''')

        exceptions_thrown = set()
        total_exceptions = 0
        while keep_bot_on:
            while time.time() - last_time_bot_ran <= 60 and keep_bot_on:
                time.sleep(1)
            if not keep_bot_on:
                break
            last_time_bot_ran = time.time()
            print time.ctime()
            for subreddit in subreddits:
                # Since every API call is 2 seconds apart
                # we add every post to the database within API calls
                try:
                    for post in itertools.chain(subreddit.get_hot(limit=100), subreddit.get_new(limit=100)):
                        if post.is_self:
                            continue
                        #print post
                        insert_post_into_db(
                            cur,
                            url=post.url,
                            author=post.author.name,
                            score=int(post.score),
                            created_time=int(post.created),
                            subreddit_url=post.subreddit._url)
                    cur.execute('''
                        FLUSH TABLES
                    ''')
                except requests.exceptions.HTTPError as ex:
                    print ex
                except:
                    total_exceptions += 1
                    if total_exceptions % 10000 == 0:
                        total_exceptions = 0
                        exceptions_thrown.clear()

                    exception = ''.join(traceback.format_tb(sys.exc_info()[2]))
                    if exception in exceptions_thrown:
                        continue
                    exceptions_thrown.add(exception)
                    send_email(exception)


def read_subreddits_to_monitor():
    """Reads the list of all subreddits to monitor"""
    with open("subreddits.list") as f:
        all_subreddits = f.readlines()
        all_subreddits = [subreddit.strip() for subreddit in all_subreddits if subreddit.strip()]
        return all_subreddits


if __name__ == '__main__':
    run_bot()


