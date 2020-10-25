n = int(input())


class numStr(str):
    def cmp(self, other):
        s1 = str(self)
        s2 = str(other)
        len1 = len(s1)
        len2 = len(s2)
        max_test = len1 * len2
        for i in range(max_test):
            p1 = i % len1
            p2 = i % len2
            if s1[p1] > s2[p2]:
                return 1
            elif s1[p1] < s2[p2]:
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


a = []
for i in range(n):
    t = input()
    a.append(numStr(t))

a.sort(reverse=True)
print(*a, sep="")
