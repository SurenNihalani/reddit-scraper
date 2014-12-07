__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np
import csv

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    lengths = []
    for row in reader:
        index, link, author, subreddit_link, created_time, score, json_info = row
        created_time = float(created_time)
        score = int(score)
        line = json.loads(json_info)
        #print line        
        if len(line) >= 2:
            line.sort(key=lambda s: s[2])
            original_author = line[0][0]
            #print original_author
            lengths.append(len([item for item in line if item[0] == original_author]))
    #print lengths
    arr=np.array(lengths)
    print "The original author posts more than once ",float(len(arr[arr>1]))/len(arr)*100,"%% times"
    c = Counter(lengths)
    c[1] = 0
    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 1, 1), facecolor='green', alpha=0.75, log=True)
    pyplot.xlabel('Number of times original author posted')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of posts by original author')
    pyplot.grid(True)
    pyplot.savefig('original_author' + '.png')