# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Embedded file name: primes.py
# Compiled at: 2024-04-04 12:22:57
# Size of source mod 2**32: 610 bytes
import os
lower = 1
upper = 50
os.system("clear")
print("Numeros primeos entre %d y %d son: \n" % (lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("%d " % num)

# okay decompiling old_primes.pyc
