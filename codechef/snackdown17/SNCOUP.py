#!/usr/bin/env python

T = int(raw_input().strip())

for i in xrange(T):
	n = int(raw_input().strip())
	a = []
	for ii in xrange(2):
		aa = raw_input().strip()
		a.append(aa)

	check_hor = True
	fence_count = 0
	snake_up, snake_down = False, False

	for j in xrange(n):
		up = a[0][j]
		down = a[1][j]

		if up=='*' and down=='.':
			if snake_up:
				fence_count += 1
				snake_down = False
			elif snake_down and check_hor:
				fence_count +=1 
				check_hor = False
			snake_up = True
		elif up=='.' and down=='*':
			if snake_down:
				fence_count +=1
				snake_up = False
			elif snake_up and check_hor:
				fence_count += 1
				check_hor = False
			snake_down = True
		elif up=='*' and down=='*':
			if check_hor:
				fence_count += 1
				check_hor = False
			if snake_up or snake_down:
				fence_count += 1
			snake_down = True
			snake_up = True

	print fence_count