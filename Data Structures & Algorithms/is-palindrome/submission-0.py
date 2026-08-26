class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = ""
        for i in s:
            if i.isalnum():
                i = i.lower()
                answer += i

        if answer == answer[::-1]:
            return True
        return False