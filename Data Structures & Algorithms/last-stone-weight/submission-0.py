class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) != 1:
            first_max = max(stones)
            stones.remove(first_max)
            second_max = max(stones)
            stones.remove(second_max)
            
            answer = first_max - second_max

            stones.append(answer)
   


        return stones[0]