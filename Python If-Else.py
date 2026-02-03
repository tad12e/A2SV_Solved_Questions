#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    def check_weirdness(n):
        if n % 2 == 1:  # Check if the number is odd
            print("Weird")
        else:  # The number is even
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            elif n > 20:
                print("Not Weird")

    # Sample Input
    
    check_weirdness(n)
