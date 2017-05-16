#!/usr/bin/env python

def length_longest_inc_subseq(arr, n):
	l = [0]*(n)
	# arr = [50, 3, 10, 7, 8, 40, 80]
	for el in arr:
		l[0] = 1

def main():
	t = int(raw_input().strip())

	for i in xrange(t):
		n = int(raw_input().strip())
		for ii in xrange(n):
			arr = map(int, raw_input().strip().split(' '))
			length_longest_inc_subseq(arr, n)

if __name__ == '__main__':
	main()