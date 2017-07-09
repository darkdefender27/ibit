#!/usr/bin/env python
# Author: Shubham Utwal
# Problem Link: https://www.codechef.com/JULY17/problems/CHEFSIGN


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        seq = raw_input()
        max_seq_ct, curr_seq_ct = 0, 0
        m_seq_ct, c_seq_ct = 0, 0

        for i in seq:
            if i == '<':
                curr_seq_ct += 1
                if c_seq_ct > m_seq_ct:
                    m_seq_ct = c_seq_ct
                c_seq_ct = 0
            elif i == '>':
                c_seq_ct += 1
                if curr_seq_ct > max_seq_ct:
                    max_seq_ct = curr_seq_ct
                curr_seq_ct = 0

        if curr_seq_ct > max_seq_ct:
            max_seq_ct = curr_seq_ct
        elif c_seq_ct > m_seq_ct:
            m_seq_ct = c_seq_ct

        if max_seq_ct > m_seq_ct:
            print max_seq_ct + 1
        else:
            print m_seq_ct + 1


if __name__ == '__main__':
    main()
