#!/usr/bin/env python
# Author: Shubham Utwal
# Link: https://www.codechef.com/JULY17/problems/IPCTRAIN

import heapq as hq

# Max-Heap Obj
class Trainer(object):
    def __init__(self, di, ti, si):
        self._di = di
        self._ti = ti
        self._si = si

    def __cmp__(self, other):
        return -cmp(self._si, other._si)


def heap_has_element(heap):
    return (len(heap) > 0)


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        n, d = map(int, raw_input().strip().split(' '))
        trainers_arr = []
        total_sum = 0
        for __ in xrange(n):
            di, ti, si = map(int, raw_input().strip().split(' '))
            trainers_arr.append((di, ti, si))
            total_sum += (si*ti)

        # Sort the trainers array based on di
        trainers_arr.sort(key=lambda x:x[0])

        day_heap = []
        i, sadness_sum, curr_day = 0, 0, 1

        while(curr_day <= d):
            while(i<n and trainers_arr[i][0]<=curr_day):
                el = trainers_arr[i]
                trainer = Trainer(el[0], el[1], el[2])
                hq.heappush(day_heap, trainer)
                i += 1

            # Operate if day_heap has elements
            if heap_has_element(day_heap):
                max_el = hq.heappop(day_heap)
                max_el._ti -= 1
                sadness_sum += max_el._si
                if max_el._ti > 0:
                    hq.heappush(day_heap, max_el)

            curr_day += 1

        # Add up sadness of remaining trainers
        # while(heap_has_element(day_heap)):
        #     el = hq.heappop(day_heap)
        #     sadness_sum += (el._ti*el._si)

        # for j in day_heap:
        #     sadness_sum += (j._ti*j._si)
        #
        # while i<n:
        #     sadness_sum += (trainers_arr[i][1]*trainers_arr[i][2])
        #     i += 1

        print (total_sum-sadness_sum)


if __name__ == '__main__':
    main()
