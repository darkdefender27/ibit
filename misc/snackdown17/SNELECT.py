#!/usr/bin/env python

T = int(raw_input().strip())

for ii in xrange(T):
	row = raw_input().strip()
	s_count = 0
	m_count = 0
	prev = None

	for i in xrange(len(row)):

		if row[i] == 's':
			if prev == 'm':
				prev = None
			elif prev == 's':
				s_count += 1
			else:
				prev = 's'
				s_count += 1
		else:
			m_count += 1
			if prev == 's':
				s_count -= 1
				prev = None
			elif prev == 'm':
				pass
			else:
				prev = 'm'

	if s_count > m_count:
		print "snakes"
	elif s_count < m_count:
		print "mongooses"
	else:
		print "tie"



