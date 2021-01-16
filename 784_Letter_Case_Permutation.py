# time - O(2^N * N)
# space - O(N * 2 ^ N)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        pos = []

        for i in range(0, len(s)):
            if s[i].isalpha():
                pos.append(i)

        n = len(pos)
        ans = []

        for i in range(0, (1 << n)):
            part = list(s)
            for index in range(0, n):
                if (i & (1 << index)) != 0:
                    if part[pos[index]].isupper():
                        part[pos[index]] = part[pos[index]].lower()
                    else:
                        part[pos[index]] = part[pos[index]].upper()
            ans.append(''.join(part))
        return ans

# time - O(2^N * N)
# space - O(N * 2 ^ N)
def invert(s: str):
    if s.islower():
        return s.upper()
    return s.lower()


def gen(s: List[str], pos: int, ans: List[str], res: List[str]):
    if pos == len(s):
        ans.append(''.join(res))
        return
    if s[pos].isdigit():
        res.append(s[pos])
        gen(s, pos + 1, ans, res)
        res.pop()
    else:
        res.append(s[pos])
        gen(s, pos + 1, ans, res)
        res.pop()

        res.append(invert(s[pos]))
        gen(s, pos + 1, ans, res)
        res.pop()
    return pos


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        gen(list(s), 0, ans, [])
        return ans

