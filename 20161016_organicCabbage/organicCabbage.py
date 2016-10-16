#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

read = lambda: sys.stdin.readline()
mmove = [[0,1],[1,0],[0,-1],[-1,0]]

def isPossible(height, width):
	if height < 0 or height >= N or width < 0 or width >= M:
		return 'false' 
	if ground[height][width] == 1:
		return 'false'
	return 'true'

def DFS(height, width):
	for i in range(0,4):
		h = height + mmove[i][0]
		w = width + mmove[i][1]
		if isPossible(h, w) == 'true':
			ground[h][w] = 1
			DFS(h, w)
		
#def DFS(height, width):
#	stack = []
#	visited = []
#	stack.extend(width)
#
#	while(stack):
#		outputFromStack = stack.pop()
#		visited.extend(outputFromStack)
#		inputToStack = list(set(height[outputFromStack]) - set(visited))
#		inputToStack.sort()
#		stack.extend(inputToStack)
#	return visited

testCase_limit = input()
while testCase_limit > 0:
	N, M, K = map(int, read().split())
	for i in range(0, K):
		X, Y = map(int, read().split())
		ground = [[0 for col in range(X+1)] for row in range(Y+1)]
	for i in range(1, N):
		for j in range(1, M):
			if ground[i][j] == 0:
				ground[i][j] = 1
				DFS(i, j)
				whiteEarthworm = whiteEarthworm + 1;
	testCase_limit -= 1
	print whiteEarthworm
