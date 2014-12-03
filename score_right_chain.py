__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np

with open('combined.csv', 'r') as f:
    score = []
    right_chain = []
    count = 1
    for line in f:
        if count == 500:
            break;
        line = line.split(',', 6)

        line = line[-1]
        line = json.loads(line)
        count = count + 1
        if len(line) > 0:
            line.sort(key=lambda s: s[2])
            index = line.index(max(line, key=lambda s: s[3]))
            score.append(max(line, key=lambda s: s[3])[3])
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

    pyplot.scatter(right_chain, score, s=20, alpha=0.75)
    pyplot.xlabel('Right Chain Length')
    pyplot.ylabel('Score')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of scores by right chain length')
    pyplot.grid(True)
    pyplot.savefig('score_right_chain' + '.png')