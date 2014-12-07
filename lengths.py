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
        if len(line)>0:
            lengths.append(len(line))

        #if len(line) == 235:
         #   print link + " " + author + "\n"

    c = Counter(lengths)
    #pprint.pprint(sorted(c.items()))
    print "Average chain length ",np.mean(lengths)
    print "Standard deviation of chain length ",np.std(lengths)
    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 10, 10), facecolor='green', alpha=0.75, log=True)
    pyplot.xlabel('Chain length')
    pyplot.ylabel('Count')
    #pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of chain length')
    pyplot.grid(True)
    pyplot.savefig('lengths' + '.png')