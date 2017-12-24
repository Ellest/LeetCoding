def csort_int(arr):
    """
    For integers only. Not "stable"
    """
    minVal = min(arr)
    maxVal = max(arr)
    cnts = [0 for _ in range(maxVal - minVal + 1)]
    for i in arr:
        cnts[i - minVal] += 1
    pos = 0
    for i in range(len(cnts)):
        for j in range(cnts[i]):
            arr[pos] = minVal + i
            pos += 1
       
def csort(arr):
    """
    Classic implementation. "Stable"
    """
    minVal = min(arr)
    maxVal = max(arr)
    cnts = [0 for _ in range(maxVal - minVal + 1)]
    for i in arr:
        cnts[i-minVal] += 1
    cSum = 0
    for i in range(len(cnts)):
        cnts[i], cSum = cSum, cSum + cnts[i]
    res = [0 for _ in arr]
    for i in arr:
        pos = i - minVal
        res[cnts[pos]] = i
        cnts[pos] += 1
    return res

if __name__ == '__main__':
    import random
    try:
        for _ in range(50):
            arr = [random.randint(1, 100) for _ in range(20)]
            assert sorted(arr) == csort(arr), 'Test Failed'
        print('All tests pass')
    except AssertionError as error:
        print(error)
