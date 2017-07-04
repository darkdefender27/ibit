#!/usr/bin/env python
# Author: Shubham Utwal
# Incomplete

from collections import defaultdict
import itertools


class Tree(object):

	def __init__(self, connections):
		self._graph = defaultdict(tree)
		self.add_connections(connections)

	def add_connections(self, connections):
		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		self._graph[node1].add(node2)
		self._graph[node2].add(node1)

	def is_connected(self, node1, node2):
		return node1 in self._graph and node2 in self._graph[node1]

	def __str__(self):
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def check_union_set(a, b, k):
    c = a.union(b)
    if len(c) == k:
        # Check for elements in set 'c'
        set_of_k = set(xrange(1, k+1))
        if len(set_of_k.difference(c)) == 0:
            return True
        else:
            return False
    return False


def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        n, k = map(int, raw_input().strip().split(' '))
        pairs = 0
        sets = defaultdict(set)
        for i in xrange(n):
            sets[i] = set(map(int, raw_input().strip().split(' ')))

        combinations = list(itertools.combinations(xrange(n), 2))
        for a, b in combinations:
            if check_union_set(sets[a], sets[b], k):
                pairs += 1

        print pairs


if __name__ == '__main__':
    main()
