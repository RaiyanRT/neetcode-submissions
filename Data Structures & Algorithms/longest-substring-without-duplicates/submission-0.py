class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        result = 0
        l = 0
        r = 0
        size = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            size = r - l + 1
            if size > result:
                result = size
        return result