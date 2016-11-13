#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

read = lambda: sys.stdin.readline()

test_case = input()
if 20001 < test_case < 0:
	print "out of range, limit is 100!"

while test_case > 0:
	chickenPrice, toUseMoney, f, c = map(int,read().split())

	doyung = sangun = toUseMoney / chickenPrice
	doyungCoupon = sangunCoupon = doyung * c
	
	while doyungCoupon >= f:
		doyungCoupon -= f
		doyung += 1

	while sangunCoupon >= f:
		sangunCoupon = sangunCoupon - f + c;
		sangun += 1

	print "%d" % (sangun - doyung)
	test_case -= 1
