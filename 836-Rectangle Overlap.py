# time - O(1)
# space - O(1)
class Solution:
    def isRectangleOverlap(self, a: List[int], b: List[int]) -> bool:
        aMinX, aMinY, aMaxX, aMaxY = a
        bMinX, bMinY, bMaxX, bMaxY = b
        resMinX = max(aMinX, bMinX)
        resMaxY = min(aMaxY, bMaxY)
        resMaxX = min(aMaxX, bMaxX)
        resMinY = max(aMinY, bMinY)

        return resMaxX > resMinX and resMaxY > resMinY
