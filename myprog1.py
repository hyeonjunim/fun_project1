#!/usr/bin/python2.7

mysum = 0
N = raw_input("How many number to average?: ")
for i in range (0, int(N)):
        x = raw_input("number: ")
        mysum += float(x)
y = mysum / int(N)
print(y)
