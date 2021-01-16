# time : O(N)
# space: O(N)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)

        for i in range(len(T) - 1, -1, -1):
            curTemp = T[i]
            while len(stack) > 0 and curTemp >= T[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans
