#!/usr/bin/env python

def palingame_solver(s, t):
    winner = "B"
    diff = lambda l1,l2: [x for x in l1 if x not in l2]

    diff_a_b = diff(s, t)
    diff_b_a = diff(t, s)

    if len(diff_b_a) == 0 and len(diff_a_b) > 0:
        winner = "A"

    if len(diff_a_b) > 0:
        my_dict = {}
        for i in diff_a_b:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
                winner = "A"
                break

    return winner


def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        s = raw_input().strip()
        t = raw_input().strip()

        print palingame_solver(s, t)


if __name__ == '__main__':
    main()
