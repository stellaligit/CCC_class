s = [char for char in input()]
s.sort()

def word_scrambler(arr):
    if len(arr) == 1:
        return [arr[0]]
    else:
        final_result = []
        for ch in arr:
            arr_2 = arr.copy()
            arr_2.remove(ch)
            partial_result = [ch + x for x in word_scrambler(arr_2)]
            final_result.extend(partial_result)
        return final_result

ans = word_scrambler(s)
for s in ans:
    print(s)
