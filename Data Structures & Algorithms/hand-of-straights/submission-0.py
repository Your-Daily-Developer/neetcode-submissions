class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for x in sorted(hand):
            if count[x] > 0:
                for y in range(x, x + groupSize):
                    if count[y] == 0:
                        return False
                    count[y] -= 1
        
        return True