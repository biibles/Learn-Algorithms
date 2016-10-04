#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

fishbread_restnum = input("남은 붕어빵 개수: ");
if not 1 <= fishbread_restnum <= 1000:
    print "붕어빵 개수가 입력 범위에 맞지 않습니다!"
    sys.exit();

price = raw_input("붕어빵 가격: ")
price_array = []
price_array = price.split()

if not fishbread_restnum == len(price_array):
    print "붕어빵 가격 입력 갯수가 맞지 않습니다!"
    sys.exit();

fishbread_price = []
for i in range(0, len(price_array)):
    if not 1 <= int(price_array[i]) <= 10000:
        "붕어빵 가격이 범위에 맞지 않습니다! (1원 부터 10000원까지 설정할 수 있어욥 '오')"
    fishbread_price.append(int(price_array[i]));

fishbread_set_price = []
for i in range(1, len(fishbread_price)):
    set_number = fishbread_restnum / i
    rest_number = fishbread_restnum % i
    set_price = (set_number * fishbread_price[i-1]) + (rest_number * fishbread_price[rest_number-1])
    fishbread_set_price.append(set_price)

print("가장 이득이 큰 세트의 가격은 %s원" % max(fishbread_set_price))
