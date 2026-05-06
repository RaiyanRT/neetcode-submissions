class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        arrayOne = [0] * 26

        
        #lowercase a = 97
        offset = 97

        for char in s:
            arrayOne[ord(char) - offset] += 1

        arrayTwo = [0] * 26

        for char in t:
            arrayTwo[ord(char) - offset] += 1

        return arrayOne == arrayTwo
