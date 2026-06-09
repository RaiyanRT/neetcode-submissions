class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Create a sliding window the size of s1 and have it move across s2
        # if at any point the sliding window has a permutation of s1 then return true. 
        # Can use a dictionary that stores the letter and frequency 
        result = False

        l = 0
        r = 0 

        dictionary_s1 = {}

        for char in s1:
            if char in dictionary_s1:
                dictionary_s1[char] += 1
            else:
                dictionary_s1[char] = 1

        #create the initial dictionary and create the right pointer
        
        dictionary_s2 = {}

        # Edge case if the length of s1 is bigger than s2
        if len(s1) > len(s2):
            return False
        
        while r < len(s1):
            if s2[r] in dictionary_s2:
                dictionary_s2[s2[r]] += 1
            else:
                dictionary_s2[s2[r]] = 1
            
            r += 1
        
        # check first window
        if dictionary_s2 == dictionary_s1:
            return True

        #Now Slide through the whole thing with a fixed size updating the dictionary and then checking

        # slide window
        while r < len(s2):
            
            # add right character
            if s2[r] in dictionary_s2:
                dictionary_s2[s2[r]] += 1
            else:
                dictionary_s2[s2[r]] = 1

            # remove left character
            if dictionary_s2[s2[l]] == 1:
                del dictionary_s2[s2[l]]
            else:
                dictionary_s2[s2[l]] -= 1

            l += 1
            r += 1

            if dictionary_s2 == dictionary_s1:
                return True

        return False