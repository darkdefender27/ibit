#!/usr/bin/env python
# TODO://Incomplete

def check_same_char_present(s):
    return s and s == len(s) * s[0]


def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        p, q = map(str, raw_input().strip().split(' '))

        i, j, result = 0, 1, "YES"
        while j<len(q):
            if q[j] != q[i]:
                is_same = check_same_char_present(p[i:j])
                i = j
                if not is_same:
                    result = "NO"
                    break

            j += 1

        is_same = check_same_char_present(p[i:j])
        if not is_same:
            result = "NO"

        print result


if __name__ == '__main__':
    main()
