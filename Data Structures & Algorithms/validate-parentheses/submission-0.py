class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # A dictionary mapping each closing bracket to its matching opener
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # If it's a closing bracket
            if char in matching:
                # Check if stack is empty or top plate doesn't match
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket, place it on top of the stack
                stack.append(char)

        # True if no unclosed brackets remain
        return len(stack) == 0