#User function Template for python3

class MyStack:
    
    def __init__(self):
        # Initialize an empty array to represent the stack
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        # Add the element 'data' to the top of the stack
        self.arr.append(data)

    # Function to remove an item from top of the stack.
    def pop(self):
        # Check if the stack is empty
        if len(self.arr) == 0:
            return -1
        else:
            # Remove and return the top element
            return self.arr.pop()


# Function to handle the input and process queries
    def process_queries(queries):
        stack = MyStack()  # Create an instance of MyStack
        results = []       # To store the output of pop() operations
    
        for query in queries:
            if query[0] == 1:
                # Push operation: query[1] contains the element to push
                stack.push(query[1])
            elif query[0] == 2:
                # Pop operation: append the result to the results list
                results.append(stack.pop())
    
        # Print all the results for pop operations
        print(", ".join(map(str, results)))
        


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