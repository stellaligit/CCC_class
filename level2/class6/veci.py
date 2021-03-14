x = [int(i) for i in input()]

def veci(arr):
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[1] * 10 + arr[0]
        else:
            return 0
    elif len(arr) < 2:
        return 0
    num = arr[0]
    arr.remove(arr[0])
    test = veci(arr)
    if test != 0:
        test += num * (10 ** len(arr))
        return test
    else:
        arr.sort()
        for i in range(len(arr)):
            if arr[i] > num:
                temp = arr[i]
                arr[i] = num
                num = temp
                break
        else:
            return 0
    
        for i in range(len(arr)):
            num = 10 * num + arr[i]
        return num

print(veci(x))