#!/usr/bin/env python

q = eval(raw_input())

for i in range(q):
	result = "Yes"
	
	n = eval(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))

	j = 0
	while j<n-1:
		if(arr[j] - arr[j+1] == 1):
			arr[j], arr[j+1] = arr[j+1], arr[j]
		elif (arr[j] - arr[j+1]) > 1:
			result = "No"
			break
		j = j + 1

	print result