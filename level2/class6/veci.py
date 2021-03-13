x = [int(i) for i in input()]

def veci(arr):
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[1] * 10 + arr[0]
    elif len(arr) < 2:
        return 0
    num = arr[0]
    arr = arr.remove(arr[0])
    test = veci(arr)
    if test != 0:
        test += num * (10 ** len(arr))
    else:
        pass