def weightedMean(X, W, n):
    sum_weight = 0
    for i in range(n):
        sum_weight += (X[i] * W[i])
        
    return print(round((sum_weight / sum(W)), 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights, n)
