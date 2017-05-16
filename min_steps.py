#!/usr/bin/env python

def coverPoints(X, Y):
        i = 0
        j = 1 + i
        steps = 0
        while (j < len(X)): # or len(Y)
        	steps = steps + max(abs(Y[j]-Y[i]), abs(X[j]-X[i]))
        	i = i+1
        	j = j+1

        print steps

def main():
	X = [-7, -13]
	Y = [1, -5]
	coverPoints(X, Y)

if __name__ == '__main__':
	main()