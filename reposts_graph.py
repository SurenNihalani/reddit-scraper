__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot

counts = {}
with open('subreddits.list') as f:
    all_subreddits = f.readlines()
    all_subreddits = [subreddit.strip() for subreddit in all_subreddits if subreddit.strip()]
    for subr in all_subreddits:
        views = { 'first' : 0, 'repost' : 0 }
        counts[subr] = views
print counts
with open('data2.csv', 'r') as f:
    lengths = []
    for line in f:
        line = line.split(',', 6)
        post_subreddit = line[3][24:-1]
        post_time = line[4]
        post_author = line[2]
        line = line[-1]
        line = json.loads(line)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            original_author = line[0][0]
            original_subreddit = line[0][1][24:-1]
            original_time = line[0][2]
            if post_subreddit == original_subreddit and post_time == original_time and post_author == original_author :
                counts[post_subreddit]['first'] += 1
            else:
                counts[post_subreddit]['repost'] += 1
            #lengths.append(len([item for item in line if item[0] == original_author]))
        else:
            counts[post_subreddit]['first'] += 1
    print counts

    X = range(12)
    repost = []
    original = []
    for k in counts:
        repost.append(counts[k]['repost'])
        original.append(counts[k]['first'])
    print len(repost)
    print original
    pyplot.bar(X, repost, color = 'b')
    pyplot.bar(X, original, color = 'r', bottom = repost)
    #pyplot.legend((repost[0], repost[1], ('repost','original'))
    pyplot.xlabel('Subreddit')
    pyplot.ylabel('Number of posts')
    pyplot.title('Number of reposts by subreddit')
    pyplot.xticks(X,all_subreddits, size='10', rotation=45)
    pyplot.tight_layout(pad=1.2)
    #pyplot.margins(0.9)
    pyplot.savefig('reposts' + '.png')