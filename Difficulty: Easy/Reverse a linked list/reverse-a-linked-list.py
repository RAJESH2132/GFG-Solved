#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # write your code here
        # Initialize 'temp' at the
        # head of the linked list
        temp = head
        
        # Initialize 'prev' to None,
        # representing the previous node 
        prev = None
        
        while temp is not None:
            # Store the next node in 'front'
            # to preserve the reference
            front = temp.next
            # Reverse the direction of the current
            # node's 'next' pointer to point to 'prev'
            temp.next = prev
            # Move 'prev' to the current 
            # node, for the next iteration
            prev = temp
            # Move 'temp' to 'front' node
            # advancing traversal
            temp = front
    
        # Return the new head
        # of the reversed linked list
        return prev
    
#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):

        arr = [int(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends