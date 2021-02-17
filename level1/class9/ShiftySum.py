n = int(input())
k = int(input())

# value = n
# for i in range(k):
#     value += n * (10 ** (i + 1))

# value = n
# for i in range(k):
#     n *= 10
#     value += n

value = n * (10 ** (k + 1) - 1) // 9

print(value)
