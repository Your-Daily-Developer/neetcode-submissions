class Solution:
    def encode(self, strs: List[str]) -> str:
        # Format: length + '#' + string  for every string
        # Example: ["hello", "world"] → "5#hello5#world"
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            # 1. Find the '#' that separates length from the string
            j = i
            while s[j] != "#":
                j += 1

            # 2. Get the length
            length = int(s[i:j])

            # 3. Extract the string of that length
            word = s[j+1 : j+1+length]
            res.append(word)

            # 4. Move pointer past this word
            i = j + 1 + length

        return res