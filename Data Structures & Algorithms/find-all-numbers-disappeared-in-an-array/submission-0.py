class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Convert the nums array to a set to eliminate any dupicates
        nums_set = set(nums)
        #create an array to store any missing numbers
        missing = []
        # store the n and add 1 for python loop
        n = len(nums) +1 
        #loop through the max n expected and compare whats in my
        # set , if not found then add to the missing array
        for i in range(1, n):
            if i not in nums_set:
                missing.append(i)
        #return the missing array
        return missing
        