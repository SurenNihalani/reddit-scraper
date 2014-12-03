import csv
import json
import pprint
from collections import Counter
from matplotlib import pyplot
import numpy as np

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    score_list = []
    for row in reader:
        index, link, author, subreddit_link, created_time, score, json_info = row
        created_time = float(created_time)
        score = int(score)
        line = json.loads(json_info)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            score_list.append(max(line, key=lambda s: s[3])[3])

	c = Counter(score_list)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    #pyplot.hist(x, bins=bins, facecolor='green', alpha=0.75)
    pyplot.hist(x,bins=np.arange(min(x),max(x)+1,1),facecolor='green', alpha=0.75)
    pyplot.xlabel('Maximum scores')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of maximum scores')
    pyplot.grid(True)
    pyplot.savefig('max_score_distribution' + '.png')

 			