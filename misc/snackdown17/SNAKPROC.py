#!/usr/bin/env python

R = int(raw_input().strip())

for i in xrange(R):
	L = int(raw_input().strip())
	report = raw_input()

	result = "Valid"
	stack = []

	for i in xrange(L):
		if(report[i] == 'H'):
			if(len(stack) != 0 and stack.pop() == 'H'):
				result = "Invalid"
				break
			else:
				stack.insert(0, 'H')
		elif(report[i] == 'T'):
			if(len(stack) == 0):
				result = "Invalid"
				break
			else:
				stack.pop()
		else:
			pass

	if(len(stack) != 0 and stack.pop() == 'H'):
		result = "Invalid"

	print result