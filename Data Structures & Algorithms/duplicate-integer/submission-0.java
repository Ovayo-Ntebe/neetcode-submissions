class Solution {
    public boolean hasDuplicate(int[] nums) {

        //boolean to see if found
        boolean hasDup = false;
       //arrCOunt var to increment for each number in arr
             int counter = 0;
        while(counter < nums.length && hasDup != true)
        {
             
        //var to hold current number to compare
             int curNum = nums[counter];

            int charCounter = 0;

             for(int i : nums)
             {
              if(i == curNum)
              {
                //increase char counter
                charCounter++;

                //found dup - if charCounter is > 1 
                if(charCounter > 1)
                {
                    hasDup = true;
                     return hasDup;
                }
                
              }
              
             }

             //if nothing is found yet, increase counter and compare next char
             counter++;
        }
       
       //if not found return false
       return false; 
    }
}