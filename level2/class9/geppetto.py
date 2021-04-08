import sys
input = sys.stdin.readline
n = int(input())
def fun(idx, comb):
    if idx > n:
        print(comb)
        return
    fun(idx+1, comb)
    comb.append(idx)
    fun(idx+1, comb)
    comb.pop()
 
fun(1, [])
