class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = ""
        answer_list = []
        for i in digits:
            value += str(i)

        value = int(value) + 1
        value = str(value)
        
        for i in value:
            answer_list.append(int(i))
        return answer_list