# -*- coding: utf-8 -*-
import random

fishbread_restnum = random.randint(1, 1000)
print("남은 붕어빵 개수: %d\n" % fishbread_restnum)

fishbread_price = []
for i in range(0, fishbread_restnum):
    price = random.randint(1, 10000)
    fishbread_price.append(price)
    print("붕어빵 가격 : %d"% fishbread_price[i])
print "\n"

fishbread_set_price = []
for i in range(1, len(fishbread_price)+1):
    set_number = fishbread_restnum / i
    rest_number = fishbread_restnum % i
    set_price = (set_number * fishbread_price[i-1]) + (rest_number * fishbread_price[rest_number-1])
    fishbread_set_price.append(set_price)

print("가장 이득이 큰 세트의 가격은 %d원" % max(fishbread_set_price))
