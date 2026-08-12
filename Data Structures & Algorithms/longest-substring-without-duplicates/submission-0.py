class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #define variables
        l = 0
        n = len(s)
        longest = 0 #longest is the max of the window without duplicates
        sett = set() #use set since it doesnt allow duplicates

        # for loop each r(index) till n and for each r check if its not in set already
        for r in range(n):
            while s[r] in sett:
                #if a letter is in the set already remove it from the set then shift l
                sett.remove(s[l])
                l+=1 

            #if not in set calc the new window size 
            window = (r-l) + 1 #This is a;ways the formula (r-l) + 1
            longest = max(longest, window)
            sett.add(s[r]) #if there was no dup then add the new letter

        return longest
        