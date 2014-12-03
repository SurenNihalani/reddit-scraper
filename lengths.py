__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np

with open('combined.csv', 'r') as f:
    lengths = []
    count = 1
    for line in f:
        if count == 500:
            break

        count = count + 1
        line = line.split(',', 6)

        line = line[-1]
        line = json.loads(line)
        lengths.append(len(line))

    c = Counter(lengths)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 1, 1), facecolor='green', alpha=0.75)
    pyplot.xlabel('Chain length')
    pyplot.ylabel('Count')
    #pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of chain length')
    pyplot.grid(True)
    pyplot.savefig('lengths' + '.png')