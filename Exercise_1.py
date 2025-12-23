class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
  #Time Complexity : O(1)
  #Space Complexity :O(1)
  #Did this code successfully run on Leetcode :
  #Any problem you faced while coding this : Have learned concept of stack

  #Your code here along with comments explaining your approachclass myStack:
  #Stack -LIFO
  #isEmpty- checking if the length of the stack is 0, return True else False
  # Push - Adding element to the top
  # Pop - Removing the element from the top
  # Peek - Accessing the top element
  # size - return the length of the stack
  # show - displays the stack

     def __init__(self):
          self.stack=[]

     def isEmpty(self):
         if len(self.stack) == 0:
             return True
         return False

     def push(self, item):
         self.stack.append(item)

     def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

     def peek(self):
        if self.isEmpty():
             return None
        return self.stack[-1]

     def size(self):
         return  len(self.stack)
     def show(self):
         return self.stack

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
