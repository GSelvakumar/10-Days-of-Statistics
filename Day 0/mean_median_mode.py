n = int(input())
arr = list(map(int, input().split()))[:n]

# Sort the array
sort_arr = sorted(arr)

# Mean
mean_val = sum(sort_arr) / len(sort_arr)
print(mean_val)

# Median
median_val = (sort_arr[len(sort_arr)//2 -1] + sort_arr[len(sort_arr)//2]) / 2
print(median_val)

# Mode
count = {}
max_count = 0
mode_val = sort_arr[0]
for i in sort_arr:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
for i in count:
    if count[i] > max_count:
        max_count = count[i]
        mode_val = i
print(mode_val)
        

# --------------- USING COLLECTIONS FOR MODE ---------

# from collections import Counter
# count = Counter(sort_arr)
# mode_val = count.most_common(1)[0][0]
# print(mode_val)



# ---------------- USING PACKAGES -----------------
# import numpy as np
# import scipy as sp

# n = int(input())
# arr = list(map(int, input().split()))[:n]
# print(np.mean(arr))
# print(np.median(arr))
# print(int(sp.stats.mode(arr)[0]))
 

