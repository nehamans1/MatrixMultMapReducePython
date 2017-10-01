#!/usr/bin/python

import sys

last_key = None
this_key = None
#running_total = 0
vals = []
mydict = {}

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split(":", 1)
    #print("{0}:{1}".format(this_key, value))
    value = eval(value)
    if(last_key == this_key):
		#running_total += value
        vals.append(value)
    else:
        if last_key:
			#print( "{0}:{1}".format(last_key, running_total) )
            #print("{0}:{1}".format(last_key, vals))
            mydict[last_key] = vals
            vals=[]

        vals.append(value)
        last_key = this_key

if last_key == this_key:
	#print( "{0}\t{1}".format(last_key, running_total))
    mydict[last_key]=vals
	#print("{0}:{1}".format(last_key, vals))

for key in mydict:
    print('{0}:{1}'.format(key, mydict[key]))
    elems=[]
    A_elems=[]
    B_elems=[]
    sum=0
    elems = mydict[key]
    for e in elems:
        if e[0]=='A':
            A_elems.append(e[1:])
        else:
            B_elems.append(e[1:])
    for a in A_elems:
        for b in B_elems:
            if(a[1]==b[0]):
                sum=sum+(a[2]*b[2])
    print('{0}:{1}'.format(key,sum))

