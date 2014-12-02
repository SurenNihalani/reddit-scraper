__author__ = 'sn'
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'

print 'Argument List:', str(sys.argv)

if len(sys.argv) == 1:
    print "give me some files to combine"
visited = set()

with open('combined.csv', 'w') as w:
    for file in sys.argv[1:]:
        with open(file, 'r') as source:
            for line in source:
                full_line = line
                line = line.strip()
                line = line.split(',', 6)

                print line
                row_number = int(line[0])
                if row_number in visited:
                    continue
                visited.add(row_number)
                w.write(full_line)

