#plots for reddit
import json
from collections import Counter
from matplotlib import pyplot
import numpy as np

with open('combined.csv', 'r') as f:
    lengths = []
    uniqueAuthorsNo = []
    i=1
    for line in f:
        line = line.split(',',6)

        line = line[-1]
        #print i
        
        line = json.loads(line)

        i=i+1
        if i==519:
        	break

        if len(line) > 1:
            line.sort(key=lambda s: s[2])
            uniqueAuthors=[]#list(set(list(line[0])))
            for j in range(len(line)):
            	uniqueAuthors.append(line[j][0])
            uniqueAuthors=list(set(uniqueAuthors))
            #uniqueAuthorsNo.append(float(len(uniqueAuthors)/len(line)))
            uniqueAuthorsNo.append(float(len(uniqueAuthors))/len(line))
            lengths.append(len(line))
    #print lengths
    #print uniqueAuthorsNo
    c = Counter(uniqueAuthorsNo)

    x = list(c.elements())
    #print x
    #bins = [i * 1 for i in range(10)]

    pyplot.hist(x, bins=np.arange(min(x), max(x) + 0.1, 0.1), facecolor='green', alpha=0.75)
    #pyplot.hist(x,bins=20)
    pyplot.xlabel('Number of unique authors/ Chain length')
    pyplot.ylabel('Count')
    # pyplot.suptitle(r'pvalue')

    pyplot.title(r'Distribution of different authors reposting')
    pyplot.grid(True)
    pyplot.savefig('unique_authors' + '.png')
