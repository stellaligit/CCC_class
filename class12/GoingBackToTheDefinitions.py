n = int(input())


class numStr(str):
    def __eq__(self, other):
        return super().__eq__(self, other)

    def __ne__(self, other):
        return super().__ne__(self, other)

    def __gt__(self, other):
        return self + other > other + other

    def __lt__(self, other):
        return self + other < other + other

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


a = []
for i in range(n):
    t = input()
    a.append(numStr(t))

a.sort(reverse=True)
print(*a, sep="")
