#!/bin/usr/python

## 1 - create list of numbers which are multiple of 3 and 7 between 1 to 500

print "Quest 1:"
L1 = list(range(0,500,21))
print "List:", L1
print "Mean:", sum(L1)/len(L1)


print "quartile"

q1 = L1[len(L1)/4]
print "1st Quartile:",q1  

q2= L1[len(L1)/2]

q3 = L1[3*len(L1)/4]

print "q2:",q2
print "q3:",q3
