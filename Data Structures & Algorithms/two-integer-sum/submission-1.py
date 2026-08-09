class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I will attempt a brute force of this first
        #Loop through each index and compare if its sum is equal to 
        #target and so on so on
        #O(n^2) time 
        indices = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    indices.append(i)
                    indices.append(j)
        return indices

                

        