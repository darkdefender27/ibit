#!/usr/bin/env python

from collections import defaultdict


class Graph(object):

	def __init__(self, connections):
		self._graph = defaultdict(set)
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


def dfs(graph, start, visited):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            adj = graph[vertex]
            stack.extend(adj - visited)

    return visited


def get_no_of_components(graph):
	visited, component_count = set(), 0
	for k in graph:
		if k not in visited:
			component_count += 1
			v = dfs(graph, k, visited)
	return component_count


def main():

	T = int(raw_input().strip())
	for ii in xrange(T):
		n, m = map(int, raw_input().strip().split(' '))
		connections = []
		for i in xrange(m):
			c = map(int, raw_input().strip().split(' '))
			connections.append(c)
		g = Graph(connections)
		result = []
		degrees = {}
		for k in g._graph:
			degrees[k] = len(g._graph[k])

		for d in xrange(n):
			clone = g._graph
			minus = set()
			for k in degrees:
				if degrees[k]<=d :
					minus.add(k)

			for m in minus:
				for key in clone:
					if key == m:
						clone[key] = set()
					else:
						if m in clone[key]:
							clone[key].remove(m)

			no_of_components = get_no_of_components(clone)
			ans = no_of_components - 1
			result.append(ans)

		for ans in result:
			print ans,


if __name__ == '__main__':
	main()
