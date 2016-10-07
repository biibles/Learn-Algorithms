#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

read = lambda: sys.stdin.readline()

def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*factorial(num-1)

def connect(N, M):
    return factorial(M)/(factorial(M-N)*factorial(N))

caseLimit = input("몇번 테스트 할 건지: ")

for t in range(0, caseLimit):
    N, M = map(int, read().split())
    print(int(connect(N, M)))
