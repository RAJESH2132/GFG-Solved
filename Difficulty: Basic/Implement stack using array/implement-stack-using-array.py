#User function Template for python3

#Back-end complete function Template for Python 3
class MyStack:
    def __init__(self):
        self.arr = []

    #Function to push an integer into the stack.
    def push(self, data):
        self.arr.append(data)
        
    #Function to remove an item from top of the stack.
    def pop(self):

        #if stack is empty, we return -1 else we return the top element.
        if len(self.arr) == 0:
            return -1
            
        return self.arr.pop()

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()

# } Driver Code Ends