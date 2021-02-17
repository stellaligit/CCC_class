class numStr(str):
    def cmp(self, other):
        s1 = str(self) + str(other)
        s2 = str(other) + str(self)
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __ne__(self, other):
        return self.cmp(other) != 0

    def __gt__(self, other):
        return self.cmp(other) == 1

    def __lt__(self, other):
        return self.cmp(other) == -1

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __le__(self, other):
        return self.cmp(other) <= 0


n = int(input())

a = []
for i in range(n):
    t = input()
    a.append(numStr(t))

a.sort(reverse=True)
print(*a, sep="")
