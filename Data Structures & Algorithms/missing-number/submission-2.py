class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #finf the max its the len of the nums array
        max = len(nums)
        nums.sort()

        #compare the index with the value in the array
        for i in range(max):
            if nums[i] != i: # missing num found while in the array
             return i
           
        #if have not returned at all then the last num was the missing num
        return max


        #find the max of list, but sort it first
       # nums.sort()
       # max = nums[-1] + 1 
        # this list will have all the required nums in order
        #compareList = [i for i in range(max)]

       # for i in range(max):
        #    if nums[i] != compareList[i]:
         #       return int(compareList[i])
            