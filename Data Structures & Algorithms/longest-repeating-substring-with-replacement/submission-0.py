class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # Keep track of the most frequent character seen in the window
            max_freq = max(max_freq, count[char])

            # If the letters needing replacement exceed k, shrink the window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Window is valid; update the maximum length found
            max_len = max(max_len, right - left + 1)

        return max_len