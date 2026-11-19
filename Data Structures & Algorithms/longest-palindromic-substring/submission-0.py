class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After the loop, left and right are one step too far
            return right - left - 1   # length of the palindrome
        
        for i in range(len(s)):
            # Odd length (center at i)
            len1 = expand(i, i)
            # Even length (center between i and i+1)
            len2 = expand(i, i + 1)
            
            current_max = max(len1, len2)
            
            if current_max > max_len:
                max_len = current_max
                # Calculate the starting index of this palindrome
                start = i - (current_max - 1) // 2
        
        return s[start : start + max_len]