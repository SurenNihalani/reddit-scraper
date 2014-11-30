__author__ = 'sn'
import json
from collections import Counter
from matplotlib import pyplot

with open('data2.csv', 'r') as f:
    lengths = []
    for line in f:
        line = line.split(',', 6)

        line = line[-1]
        line = json.loads(line)
        lengths.append(len(line))

    c = Counter(lengths)

    x = list(c.elements())
    print x
    bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=bins, facecolor='green', alpha=0.75)
    pyplot.xlabel('Chain length')
    pyplot.ylabel('Count')
    pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of chain length')
    pyplot.grid(True)
    pyplot.savefig('lengths' + '.png')