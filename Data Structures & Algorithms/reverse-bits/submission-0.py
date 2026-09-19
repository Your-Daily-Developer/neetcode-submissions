class Solution:
    def reverseBits(self, n: int) -> int:
        str_value = format(n, '032b')[::-1]
        return int(str_value, 2)