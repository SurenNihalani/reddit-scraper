__doc__ = """

A reddit bot that snapshots the hot page (upto 100 submissions) for 30 subreddits from a file

"""

import praw
import pprint
import signal
import time


pp = pprint.PrettyPrinter(indent=4)

keep_bot_on = True


def turn_bot_off_on_ctrl_c(signal, frame):
    """The bot runs an while True loop. Ctrl c breaks that loop so we can clean up gracefully"""
    global keep_bot_on
    keep_bot_on = False


signal.signal(signal.SIGINT, turn_bot_off_on_ctrl_c)


def insert_post_into_db(url="", author="", score=0, created_time=0, subreddit_url=""):
    """Stores a hot post into the db for analysis later"""
    pass


def run_bot():
    """Runs the bot. Everything you need to know about the bot is in this function"""
    r = praw.Reddit('A school project bot to study distribution of links amongst subreddits')
    r.set_oauth_app_info(
        client_id='GTlkDtvm2KkPjA',
        client_secret='iJsUT9SQSI4jiIZHZxUtAqQhJ-Q',
        redirect_uri='http://127.0.0.1:5000/')
    r.login(username="your_id_HERE", password="PUT_YOUR_PASSWORD_HERE")

    subreddits = [
        r.get_subreddit(subreddit_name=sub_reddit_name)
        for sub_reddit_name in read_subreddits_to_monitor()]

    last_time_bot_ran = time.time()

    while keep_bot_on:
        if time.time() - last_time_bot_ran <= 60:
            time.sleep(1)
        last_time_bot_ran = time.time()

        for subreddit in subreddits:
            # Since every API call is 2 seconds apart
            # we add every post to the database within API calls
            for post in subreddit.get_hot(limit=100):
                if post.is_self:
                    continue

                insert_post_into_db(
                    url=post.url,
                    author=post.author.name,
                    score=int(post.score),
                    created_time=int(post.created),
                    subreddit_url=post.subreddit._url)

                break

        break


def read_subreddits_to_monitor():
    """Reads the list of all subreddits to monitor"""
    with open("/Users/sn/Dropbox (Personal)/dev/social_computing/reddit-scraper/subreddits.list") as f:
        all_subreddits = f.readlines()
        all_subreddits = [subreddit.strip() for subreddit in all_subreddits if subreddit.strip()]
        return all_subreddits


if __name__ == '__main__':
    run_bot()
    sql.close()


