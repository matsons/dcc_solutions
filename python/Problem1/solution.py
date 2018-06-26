def elements_sum(arr, k):
    # basic edge case handling
    if arr is None or len(arr) == 0 or k is None:
        return false # or throw ValueError?
    l = {}
    for i in arr:
        if k - i in l:
            return True
        else:
            l[i] = i
    return False

# drive
print(elements_sum([1,2], 3)) # expect true
print(elements_sum([1,3], 3)) # expect false
print(elements_sum([1,2,-1,6,4], 0)) # expect true