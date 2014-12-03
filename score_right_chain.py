__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np
import csv

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    score_list = []
    right_chain = []
    for row in reader:
        index, link, author, subreddit_link, created_time, score, json_info = row
        created_time = float(created_time)
        score = int(score)
        line = json.loads(json_info)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            index = line.index(max(line, key=lambda s: s[3]))
            score_list.append(max(line, key=lambda s: s[3])[3])
            right_chain.append(len(line) - index -1)
            #original_author = line[0][0]
            #print original_author
            #lengths.append(len([item for item in line if item[0] == original_author]))
    #print lengths
    #lc = Counter(left_chain)
    #rc = Counter(right_chain)

    #x = list(lc.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.scatter(right_chain, score_list, s=20, alpha=0.75)
    pyplot.xlabel('Right Chain Length')
    pyplot.ylabel('Score')
    # pyplot.suptitle(r'pvalue')

    #pyplot.title(r'Distribution of scores by right chain length')
    pyplot.grid(True)
    pyplot.savefig('score_right_chain' + '.png')