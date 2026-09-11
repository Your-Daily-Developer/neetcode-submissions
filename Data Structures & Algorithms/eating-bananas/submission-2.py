class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
    
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                right = mid          # try slower speed
            else:
                left = mid + 1       # need faster speed
        
        return left