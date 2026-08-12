from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # two pointers 
        #use a deque and peak from left and right then if equal continue
        #These 2 suggestions at the top wont work(not only checking text but the order so use stacks )
        #init the stack
        stack = []
        #do a loop to check every char if its opening or closinh
        for c in s:
            if c == '(' or  c == '{' or  c == '[':
                #add to the stack
                stack.append(c)
            else:
                #check if the stack is empty..if it return false
                if len(stack) == 0:
                    return False
                
                #check the last open char in stack
                last = stack[-1]

                #check if it matches anyone
                if c== ')' and last == '(':
                    stack.pop()
                elif c== '}' and last == '{':
                    stack.pop()
                elif c== ']' and last == '[':
                    stack.pop()
                else:
                    return False
        #done
        return len(stack) == 0
                


            

        