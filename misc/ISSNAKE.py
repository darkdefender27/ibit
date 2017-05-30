#!/usr/bin/env 

T = int(raw_input().strip())

for i in xrange(T):
	n = int(raw_input().strip())
	a = []
	for ii in xrange(2):
		aa = raw_input().strip()
		a.append(aa)

	j, level, legend = 0, None, True

	while(j<n and (a[0][j] == '.' and a[1][j] == '.')):
		j += 1
	
	while(j<n and (a[0][j] == '#' and a[1][j] == '#')):
		j += 1

	while(j<n):
		if(a[0][j] == '#' and a[1][j] == '.'):
			if level == None:
				level = 0
			elif level == 1:
				legend = False
				break
		elif(a[0][j] == '.' and a[1][j] == '#'):
			if level == None:
				level = 1
			elif level == 0:
				legend = False
				break
		elif(a[0][j] == '#' and a[1][j] == '#'):
			if level == 0:
				level = 1
			else:
				level = 0
		else:
			break

		j += 1

	while(j<n and legend == True):
		if(a[0][j] == '#' or a[1][j] == '#'):
			legend = False
		j += 1

	if(legend == False):
		print "no"
	else:
		print "yes"