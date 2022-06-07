import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


class Stack: 
    def __init__(self):
        self.arr=[]
    
    def push(self,element):
        self.arr.append(element)
    
    def popElement(self):
        return self.arr.pop()
    
    def top(self):
        if(self.isEmpty()!=True):
            return self.arr[-1]
    
    def isEmpty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
        

class Solution:   
    def isValid(self, s: str) -> bool:
        stack=Stack()
        left_braces=['(','{','[']
        right_braces=[')','}',']']
        
        for i in s:
            if(i in left_braces):
                stack.push(i)
            else:
                if(stack.isEmpty()):
                    return False
                indexOfRight=right_braces.index(i)
                indexofTop=left_braces.index(stack.top())
                if(indexOfRight!=indexofTop):
                    return False
                stack.popElement()
        if(stack.isEmpty()):
            return True
        else:
            return False

s=Solution()

print(s.isValid("{([)]}"))