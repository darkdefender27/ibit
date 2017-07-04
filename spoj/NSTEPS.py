#!/usr/bin/env python


T = int(raw_input().strip())

for _ in xrange(T):
	n = int(raw_input().strip())
	a = map(int, str(n))

	l, r  = 0, len(a)-1
	while r-l>1:
		if a[l]<a[r]:
			a[r-1] += 1
		a[r] = a[l]
		l, r = l+1, r-1

	if r>l:
		if a[r]>a[l]:
			a[l] += 1
		a[r] = a[l]

	print int(''.join(map(str,a)))
