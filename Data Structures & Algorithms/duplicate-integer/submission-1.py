class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Note to self! Sets automatically remove dupicates so to effectivly check if there is a duplicate then compare the sizes
        numSet = set(nums)
    
        if len(numSet) < len(nums):
            return True
        else:
            return False

 # potentially sets as they dont want duplicates(#if myset properly exists then it means no duplicatates so it should have defaulted to if its corerect then its false but it only works for one test case)
 #       mySet = set(nums)
 #       if mySet:
 #           return False 
 #       else:
 #           return True 

 
    