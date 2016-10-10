#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

stone_num = input()
if stone_num <= 1 or 1000 <= stone_num:
    print ("stone number is out of the range!!")
    sys.exit()

if stone_num % 2 == 0:
    print("CY")
else:
    print("SK")
