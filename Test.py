#import sys
#for line in sys.stdin:

line = "I love testing very much"

line = line.strip()
keys = line.split(" ")
for key in keys:
    value = 1
    print('{0}\t{1}'.format(key, value))
