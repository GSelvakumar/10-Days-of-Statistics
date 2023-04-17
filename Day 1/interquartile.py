#!/bin/python3

import math
import os
import random
import re
import sys

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = [val for val, freq in zip(values, freqs) for _ in range(freq)]
    
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
    q3 = median(len(data_high), data_high)
    
    # Interquartile Range
    Q = q3 - q1
    
    return print(float(Q))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
