class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for i in my_dict:
            if my_dict[i] == 1:
                return i