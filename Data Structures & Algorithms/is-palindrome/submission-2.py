class Solution:
    def isPalindrome(self, s: str) -> bool:
        #define the pointers
        left = 0
        right = len(s) - 1

        while left < right:

            #check for non alpha nums and skip if found
            while left < right and not s[left].isalnum():
                left+=1 
            while left < right and not s[right].isalnum():
                right-=1
            #check if they not equal ta those spots
            if s[left].lower() != s[right].lower():
                return False
            #if all is good move the pointers
            left+=1
            right-=1
        #if all good then return true
        return True
   
       
           
       





        