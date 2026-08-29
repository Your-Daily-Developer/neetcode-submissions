class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = 0, len(numbers) - 1

        while r < l:
            current_sum = numbers[r] + numbers[l]
            if current_sum == target:
                return [r+1,l+1]
            if current_sum > target:
                l -= 1
            if current_sum < target:
                r += 1

            