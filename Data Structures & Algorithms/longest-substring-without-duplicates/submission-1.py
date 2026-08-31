class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen = {}   # char -> last index it appeared at
        left = 0
        max_len = 0
    
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1   # jump left past the duplicate
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)
    
        return max_len   