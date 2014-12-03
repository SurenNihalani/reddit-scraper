__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np
import csv

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    left_chain = []
    right_chain = []
    for row in reader:
        index, link, author, subreddit_link, created_time, score, json_info = row
        created_time = float(created_time)
        score = int(score)
        line = json.loads(json_info)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            index = line.index(max(line, key=lambda s: s[3]))
            left_chain.append(index)
            right_chain.append(len(line) - index -1)
            #original_author = line[0][0]
            #print original_author
            #lengths.append(len([item for item in line if item[0] == original_author]))
    #print lengths
    lc = Counter(left_chain)
    rc = Counter(right_chain)

    x = list(lc.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 5, 5), facecolor='green', alpha=0.75, log=True)
    pyplot.xlabel('Left Chain Length')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    #pyplot.title(r'Distribution of posts by left chain length')
    pyplot.grid(True)
    pyplot.savefig('left_chain' + '.png')

    pyplot.clf()

    x = list(rc.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 1, 1), facecolor='green', alpha=0.75, log=True)
    pyplot.xlabel('Right Chain Length')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    #pyplot.title(r'Distribution of posts by right chain length')
    pyplot.grid(True)
    pyplot.savefig('right_chain' + '.png')