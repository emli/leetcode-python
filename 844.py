# time : O(N)
# space : O(1)
def nextLetter(pos: int, s: str):
    count = 0
    while pos >= 0 and (s[pos] == '#' or count > 0):
        if s[pos] == '#':
            count += 1
        else:
            count -= 1
        pos -= 1

    return pos


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = len(s) - 1
        second = len(t) - 1

        while first >= 0 or second >= 0:
            first = nextLetter(first, s)
            second = nextLetter(second, t)

            if first >= 0 and second >= 0 and s[first] == t[second]:
                first -= 1
                second -= 1
                continue
            elif first == -1 and second == -1:
                return True
            else:
                return False
        return first == -1 and second == -1
