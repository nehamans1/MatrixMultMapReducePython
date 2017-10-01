#!/usr/bin/python

import sys

#A_numrows = 4
#B_numcols = 5
A_matr = []
B_matr = []

for line in sys.stdin:
    line = line.strip()
    matr,vals = line.split(":")
    vals = vals.split(",")
    intvals = []
    if matr=='A':
        for elem in vals:
            intvals.append(int(elem))
        A_matr.append(intvals)
    else:
        for elem in vals:
            intvals.append(int(elem))
        B_matr.append(intvals)

A_rows = []
B_cols = []
A_numrows = 1
B_numcols = 1

for elem in A_matr:
    A_rows.append(elem[0])
A_numrows = max(A_rows)

for elem in B_matr:
    B_cols.append(elem[1])
B_numcols = max(B_cols)

key=()

for j in range(1,B_numcols+1):
#for j in range(1, 3):
    for i in range(1,A_numrows+1):
    #for i in range(1, 3):
        for elem in A_matr:
            if(elem[0]==i):
                key=(i,j)
                val = ['A']+ elem
                print('{0}:{1}'.format(key, val))
        for elem in B_matr:
            if(elem[1]==j):
                key=(i,j)
                val = ['B'] + elem
                print('{0}:{1}'.format(key, val))

#print("A: ", A_matr)
#print("B: ", B_matr)







