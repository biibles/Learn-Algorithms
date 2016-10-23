#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

read = lambda: sys.stdin.readline()
ground = [[0 for col in range(51)] for row in range(51)]

def DFS(height, width):
	ground[height][width] = 0

	if (height< N - 1 and ground[height + 1][width] == 1):
		DFS(height + 1, width)
	if (height > 0 and ground[height - 1][width] == 1):
		DFS(height - 1, width)
	if (width < M - 1 and ground[height][width + 1] == 1):
		DFS(height, width + 1)
	if (width > 0 and ground[height][width - 1] == 1):
		DFS(height, width - 1)


testCase_limit = input()
while testCase_limit > 0:
	whiteEarthworm = 0
	N, M, K = map(int, read().split())
	for i in range(0, K):
		X, Y = map(int, read().split())
		ground[X][Y] = 1

	for i in range(1, N):
		for j in range(1, M):
			if ground[i][j] == 1:
				whiteEarthworm = whiteEarthworm + 1;
				DFS(i, j)
	testCase_limit -= 1
	print whiteEarthworm
