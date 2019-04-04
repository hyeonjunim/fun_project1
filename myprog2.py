#!/usr/bin/python2.7

n = raw_input("Which Fibonacci Sequence?: ")

F1 = 1
F2 = 1
F3 = 0

if (n == "1") or (n == "2"):
	print 1
else:
	for i in range(2,int(n)):
		F3=F2+F1
		F1=F2
		F2=F3
		i += 1
	print F3
