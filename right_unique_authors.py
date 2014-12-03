#plots for reddit
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np
import csv

with open('final_filtered.csv') as f:
    reader = csv.reader(f)
    lengths = []
    uniqueAuthorsNo = []
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
            uniqueAuthorsNo.append(len(uniqueAuthors)-1)
            lengths.append(len(line))
    #print lengths
    #print uniqueAuthorsNo
    c = Counter(uniqueAuthorsNo)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    #pyplot.hist(x, bins=bins, facecolor='green', alpha=0.75)
    pyplot.hist(x,bins=np.arange(min(x),max(x)+1,1),facecolor='green', alpha=0.75, log=True)
    pyplot.xlabel('Unique authors in the right chain')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    #pyplot.title(r'Distribution of unique authors in the right chain')
    pyplot.grid(True)
    pyplot.savefig('right_chain_unique_authors' + '.png')
