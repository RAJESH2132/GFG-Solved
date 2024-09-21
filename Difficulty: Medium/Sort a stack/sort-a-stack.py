class Solution:
    # Function to insert an element into the stack in sorted order
    def sorted_insert(self, s, element):
        # Base case: If stack is empty or the element is greater than the top
        if not s or element > s[-1]:
            s.append(element)
        else:
            # Pop the top element and insert the current element recursively
            temp = s.pop()
            self.sorted_insert(s, element)
            # Push the popped element back
            s.append(temp)
    
    # Function to sort the stack
    def Sorted(self, s):
        # Base case: if the stack is empty, do nothing
        if not s:
            return
        
        # Pop the top element
        top = s.pop()
        
        # Sort the remaining stack recursively
        self.Sorted(s)
        
        # Insert the popped element back in sorted order
        self.sorted_insert(s, top)



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends