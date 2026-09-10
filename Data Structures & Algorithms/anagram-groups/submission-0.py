from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            # Create a count of each letter (26 letters)
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as the key
            key = tuple(count)
            groups[key].append(word)
        
        return list(groups.values())