__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np

with open('combined.csv', 'r') as f:
    lengths = []
    for line in f:
        line = line.split(',', 6)

        line = line[-1]
        line = json.loads(line)
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            original_author = line[0][0]
            #print original_author
            lengths.append(len([item for item in line if item[0] == original_author]))
    #print lengths
    c = Counter(lengths)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 1, 1), facecolor='green', alpha=0.75)
    pyplot.xlabel('Number of times original author posted')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of posts by original author')
    pyplot.grid(True)
    pyplot.savefig('original_author' + '.png')