#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head is None or head.next is None:
            return head
        
        back = None  
    
    # Initialize a pointer
    # to the current node
        current = head  
    
        # Traverse the linked list
        while current is not None:
            
            # Store a reference to
            # the previous node
            back = current.prev 
    
            # Swap the previous and next pointers
            current.prev = current.next
            
             # This step reverses the links
            current.next = back
            
            # Move to the next node
            # in the original list
            current = current.prev  
    
        # The final node in the original list
        # becomes the new head after reversal
        return back.prev 



#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = DLLNode(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.reverseDLL(head)
        printList(resHead)

# } Driver Code Ends