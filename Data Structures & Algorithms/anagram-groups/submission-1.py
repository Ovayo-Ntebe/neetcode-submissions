from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #might use Counter 
        #might use a 2d array for output.. 
        #loop through the single input array and make a counter for them. Then if not existing then add to the output array. if counter thats is equal to what is in the output array. append to that list
        anagram_map = {}

        for word in strs:
            word_count = Counter(word)
            #put the key(the dict of count) and the word it self in the dict
            #since can not use a counter as a dict key make it a tuple
            tuple_word_count = tuple(sorted(word_count.items()))
            if tuple_word_count not in anagram_map:
                anagram_map[tuple_word_count] = [] #init an empty array
                #then append at that key the work
                anagram_map[tuple_word_count].append(word)
            else:
                #if that counter dictionary already exists then append to it
                anagram_map[tuple_word_count].append(word)
        
        #put all found values in a list
        final_list = list(anagram_map.values())
        return final_list

        