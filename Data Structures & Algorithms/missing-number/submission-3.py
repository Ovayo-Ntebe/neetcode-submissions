class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      # a better approach would not using for loops which 
      #my prev solution was a O(nlogn)
      # rather compare the sums of the lists which is O(n)
      max = len(nums) + 1

      return sum(range(max)) -sum(nums)
            