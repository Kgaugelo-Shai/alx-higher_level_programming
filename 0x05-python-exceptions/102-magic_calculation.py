#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception('Too far')
            ans += a ** b / i
        except Exception:
            ans = b + a
            break
    return ans
