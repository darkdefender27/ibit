def main():
    from sys import stdin, stdout
    n, k = stdin.readline().split()
    n = int(n)
    k = int(k)

    cnt = 0
    lines = stdin.readlines()
    for line in lines:
        if int(line) % k == 0:
            cnt += 1

    stdout.write(str(cnt))

if __name__ == "__main__":
    main()
