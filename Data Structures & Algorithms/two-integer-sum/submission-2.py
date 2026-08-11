class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #okay i will create a dictonary to store the rem: imdex
        dict_nums = {}
        
        for i in range(len(nums)):
            rem = target - nums[i]
            
            # Check if the REMAINDER is a number we have already seen
            if rem in dict_nums:
                return [dict_nums[rem], i]

            # Store the current number we just saw, and its index
            dict_nums[nums[i]] = i
   
     


                

        