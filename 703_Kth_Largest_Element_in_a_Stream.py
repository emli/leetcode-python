# time - init() -> O(k+(n-k)logk)
# time - add -> O(log(K))
# space - O(K)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        self.k = k

        heapify(self.heap)

        for i in range(k, len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        if len(self.heap) >= self.k:
            return self.heap[0]
