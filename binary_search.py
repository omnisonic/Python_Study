def binary_search(list, value):
    lo, hi = 0, len(list)-1
    while lo <= hi:
        mid =(lo + hi) //2
        if list[mid] < value:
            lo = mid + 1
        elif value < list[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

list = [3, 6, 14, 16, 33, 55, 56, 89]

x = 56

print(binary_search(list, x))
