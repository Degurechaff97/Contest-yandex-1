def binary_search(arr, x, left):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if (arr[mid] < x) == left:
            lo = mid + 1
        else:
            hi = mid
    return lo

def find_prefix(dictionary, prefix, k):
    start = binary_search(dictionary, prefix, True)
    end = binary_search(dictionary, prefix[:-1] + chr(ord(prefix[-1]) + 1), True)
    
    if start + k - 1 < end and dictionary[start + k - 1].startswith(prefix):
        return start + k
    return -1

N, Q = map(int, input().split())
dictionary = [input().strip() for _ in range(N)]

for _ in range(Q):
    k, p = input().split()
    k = int(k)
    result = find_prefix(dictionary, p, k)
    print(result)