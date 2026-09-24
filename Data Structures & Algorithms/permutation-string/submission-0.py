class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Fill frequency of s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if s1Count == s2Count:
            return True

        # Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            # Add the new character (right side)
            s2Count[ord(s2[right]) - ord('a')] += 1

            # Remove the old character (left side)
            s2Count[ord(s2[left]) - ord('a')] -= 1
            left += 1

            # Check if frequencies match
            if s1Count == s2Count:
                return True

        return False