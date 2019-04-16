#!/usr/bin/python2.7

var1 = raw_input("Please enter the first list:  ")
var2 = raw_input("Please enter the second list: ")

x1 = var1.strip('[]')
y1 = var2.strip('[]')

x2 = x1.replace(' ','')
y2 = y1.replace(' ','')

list1 = x2.split(',')
list2 = y2.split(',')

int_list1 = list(set(list1).intersection(list2))
int_list2 = sorted(int_list1)
print int_list2

uni_list1 = list(set(list1).union(list2))
uni_list2 = sorted(uni_list1)
print uni_list2
