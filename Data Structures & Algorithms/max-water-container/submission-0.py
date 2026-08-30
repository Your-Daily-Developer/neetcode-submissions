class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r,l = 0, len(heights) - 1
        answer = 0
        while r < l:
            current_answer = min(heights[r],heights[l]) * (l-r)
            if current_answer > answer:
                answer = current_answer

            if heights[r] < heights[l]:
                r+=1

            else:
                l-=1

        return answer