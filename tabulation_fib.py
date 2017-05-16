#!/usr/bin/env python

def fib(n):
	arr = [0]*(n+1)
	arr[1] = 1
	
	for i in xrange(2, n+1):
		arr[i] = arr[i-1] + arr[i-2]
		
	return arr[n]

def main():
	n = raw_input().strip()
	print "Fibonacci number is ", fib(n)

if 	__name__=="main":
	main()