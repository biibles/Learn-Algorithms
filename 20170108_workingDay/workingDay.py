#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, Queue
input = sys.stdin.readline
INF = 2015147554

def pos(y, x):
	global r,c
	return y < r and y >=0 and x < c and x >= 0

r, c = map(int, input().split())
board = []

for _ in range(r):
	board.append(input().split())

n = int(input())
ne = []

for i in range(n):
	y, x = map(int, input().split())
	ne.append([y,x])

dp = [[INF for i in range(c+1)] for j in range(r + 1)]
q = Queue.PriorityQueue()

for i in range(c):
	if board[0][i] == '1':
		q.put([0, 0, i])

while not q.empty():
	p = q.get()
	dist, y, x = p[0], p[1], p[2]
	for rule in ne:
		ny = y + rule[0]
		nx = x + rule[1]
		if pos(ny, nx) and board[ny][nx] == '1' and dp[ny][nx] > dist + 1:
			dp[ny][nx] = dist + 1
			q.put([dist + 1, ny, nx])
ans = INF
for i in range(c):
	ans = min(ans, dp[r - 1][i])
if ans >= INF:
	print(-1)
else:
	print(ans)

