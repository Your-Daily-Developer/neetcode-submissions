from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)          # how many of each char we still need
        required = len(need)       # how many unique chars we still need to satisfy
        window = {}
        formed = 0                 # how many unique chars are currently satisfied

        left = 0
        min_len = float('inf')
        min_start = 0

        for right, char in enumerate(s):
            # Expand the window
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink the window as much as possible while it is still valid
            while formed == required and left <= right:
                # Update the best answer
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]