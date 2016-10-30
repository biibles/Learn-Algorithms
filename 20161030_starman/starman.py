#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

read = lambda: sys.stdin.readline()
y = [1967, 1969, 1970, 1971, 1972, 1973, 1973, 1974, 1975, 1976, 1977, 1977, 1979, 1980, 1983, 1984, 1987, 1993, 1995, 1997, 1999, 2002, 2003, 2013, 2016]
s = ["DavidBowie","SpaceOddity","TheManWhoSoldTheWorld","HunkyDory","TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars","AladdinSane","PinUps","DiamondDogs","YoungAmericans","StationToStation","Low","Heroes","Lodger","ScaryMonstersAndSuperCreeps","LetsDance","Tonight","NeverLetMeDown","BlackTieWhiteNoise","1.Outside","Earthling","Hours","Heathen","Reality","TheNextDay","BlackStar"]
r=[0 for col in range(25)]

test_case = input()
if test_case > 100:
	print "out of range, limit is 100!"

while test_case > 0:
	a, b = map(int,read().split())
	count = 0
	for i in range(0, 25):
		if y[i] >= a and y[i] <= b:
			r[count] = i
			count += 1
	print count
	for i in range(0, count):
		print "%d %s" % (y[r[i]], s[r[i]])
	test_case -= 1
