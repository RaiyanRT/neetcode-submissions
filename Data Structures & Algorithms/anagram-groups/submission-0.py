class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    

        
    
    
    
    
    
    # if the tuple key is not in the dictionary, add it 
    # append the word to the list at that tuple key 

# return all the values

    # create a dictionary 
        arrayHash = {}

        offset = 97

        # loop through the strings in the list
        
        for string in strs:
            # create an array with offset

            arrayOne = [0] * 26

            # go through all the characters in the word uysing the array
            for char in string:
                arrayOne[ord(char) - offset] += 1
            
            # turn it into a tuple as the key of the dictionary with its value pair
            key = tuple(arrayOne)

            if key not in arrayHash:
                arrayHash[key] = []
            arrayHash[key].append(string)

        return list(arrayHash.values())
            




    
    
    
    
    