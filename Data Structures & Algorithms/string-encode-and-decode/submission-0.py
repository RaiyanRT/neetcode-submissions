class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result = result + str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        number = 0
        while i < len(s):
            if s[i] == "#":
                result.append(s[i+1:i+1+number])
                i += number + 1
                number = 0
            else:
                number = number * 10 + int(s[i])
                i += 1

        return result 
