#from hacker rank problem cut the sticks
def cutTheSticks(arr):
    arr.sort()
    l1 = []
    i, m = 0, len(arr)
    while i < m:
        l1.append(m-i)
        cut = arr[i]
        while i < m and arr[i] <= cut:
            arr[i] = arr[i] - cut
            i += 1

    return l1
