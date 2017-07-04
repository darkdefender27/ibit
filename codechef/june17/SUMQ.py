#!/usr/bin/env python
# Author: Shubham Utwal
# Alias: darkdefender27


modulo = 1000000007


class Node(object):
    """
        A Binary Node with Left and Right pointers.
    """
    def __init__(self, data, left, right):
        self._data = data
        self._left = left
        self._right = right


class Tree(object):
    """
        A Tree with _root pointing to the Root if the Binary Tree.
    """
    def __init__(self):
        self._root = None

    def add_node(self, node_data):
        if self._root is None:
            self._root = Node(data, None, None)
        else:
            pass
            

def f(x, y, z):
    return ((x+y)%modulo*(y+z)%modulo))%modulo


def main():

    T = int(raw_input().strip())

    for _ in xrange(T):
        p, q, r = map(int, raw_input().strip().split(' '))
        a = map(int, raw_input().strip().split(' '))
        b = map(int, raw_input().strip().split(' '))
        c = map(int, raw_input().strip().split(' '))

        sum = 0



        """
        for ii in b:
            for i in a:
                if i <= ii:
                    for iii in c:
                        if ii >= iii:
                            sum = (sum + f(i, ii, iii))%modulo
        """

        print sum%modulo


if __name__=='__main__':
    main()
