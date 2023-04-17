#!/bin/python3

import math
import os
import random
import re
import sys

def quartiles(arr):
    # Write your code here
    def median(size, values):
        if size % 2 == 0:
            median = (values[int(size/2)-1] + values[int(size/2)]) / 2
        else:
            median = values[int(size/2)]
        return int(median)
        
    arr = sorted(arr)
    n = len(arr)
    
    if n % 2 == 0:
        data_low = arr[0:int(n/2)]
        data_high = arr[int(n/2):n]
    else:
        data_low = arr[0:int(n/2)]
        data_high = arr[int(n/2)+1:n]
        
    q1 = median(len(data_low), data_low)
    q2 = median(n, arr)
    q3 = median(len(data_high), data_high)
    
    return q1, q2, q3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
