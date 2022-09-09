#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 16:34
# @Author: xzxiao

def find_prime():
    i, total = 2, 0
    while i < 200:
        if is_prime(i):
            print(i)
            total += i
        i += 1
    print(f"The sum of prime numbers:{total}")


def is_prime(num) -> bool:
    ans = True
    i = 2
    while i < (num // 2 + 1):
        if num % i == 0:
            ans = False
            break
        i += 1
    return ans


find_prime()
