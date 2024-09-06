#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''

class Solution:
    def constructDLL(self, arr):
        head = None
        current = None
    
        # Iterate through the array
        for value in arr:
            new_node = Node(value)  # Create a new node for each element
            
            if head is None:        # If it's the first node, make it the head
                head = new_node
                current = head
            else:
                current.next = new_node  # Link current node to the new node
                new_node.prev = current  # Link the new node back to the current node
                current = new_node       # Move to the new node
        
        return head  # Return the head of the doubly linked list

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
    
def printList(node):
    tmp = node
    if tmp:
        c1, c2 = 0, 0
        while tmp.next:
            c1 += 1
            tmp = tmp.next
        while tmp.prev:
            c2 += 1
            tmp = tmp.prev
        if c1 != c2:
            print("-1")
            return
    while tmp:
        print(tmp.data, end = " ")
        tmp = tmp.next
    print()

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        printList(res)
# } Driver Code Ends
