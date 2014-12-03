#plots for reddit
import csv
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np
import pprint
import csv

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    lengths = []
    uniqueAuthorsNo = []
    best_score=[]
    for row in reader:
        index, link, author, subreddit_link, created_time, score, json_info = row
        created_time = float(created_time)
        score = int(score)
        line = json.loads(json_info)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            uniqueAuthors=[]#list(set(list(line[0])))
            index=line.index(max(line,key=lambda s:s[3]))
            for j in range(index,len(line)):
            	uniqueAuthors.append(line[j][0])
            uniqueAuthors=list(set(uniqueAuthors))
            #uniqueAuthorsNo.append(float(len(uniqueAuthors)/len(line)))
            best_score.append(max(line, key=lambda s: s[3])[3])
            uniqueAuthorsNo.append(len(uniqueAuthors)-1)
            lengths.append(len(line))
    #print lengths
    #print uniqueAuthorsNo
    c = Counter(uniqueAuthorsNo)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    #pyplot.hist(x, bins=bins, facecolor='green', alpha=0.75)
    pyplot.scatter(uniqueAuthorsNo, best_score, s=20, alpha=0.75)
    pyplot.xlabel('Unique authors in right chain')
    pyplot.ylabel('Best Score')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of scores by unique users in right chain')
    pyplot.grid(True)
    pyplot.savefig('unique_score_right_chain' + '.png')

