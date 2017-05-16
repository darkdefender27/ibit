#!/usr/bin/env python

class Interval:
	def __init__(self, s=0, end=0):
		self.start = s
		self.end = end

class Solution:
	def merge(self, intervals):
        res = []
        len_intervals = len(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)
        a = intervals[0]
        i = 1
        while i < len(intervals):
            b = intervals[i]
            if max(a.start,b.start) > min(a.end,b.end):
                res.append(a)
                a = b
            else:
                a = Interval(min(a.start, b.start), max(a.end, b.end))
            
            i = i + 1
            
        res.append(a)
            
        return res

# if __name__ == '__main__':

# 	solution = Solution()
#     solution.merge()