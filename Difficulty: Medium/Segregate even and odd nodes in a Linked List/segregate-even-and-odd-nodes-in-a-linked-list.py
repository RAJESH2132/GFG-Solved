# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        if not head:
            return None

        evenHead = even = node()  # Dummy node for even list
        oddHead = odd = node()  # Dummy node for odd list

        current = head

        while current:
            if current.data % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next

            current = current.next

        even.next = oddHead.next  # Attach odd list after even list
        odd.next = None  # Terminate the list

        return evenHead.next  # Return the head of the new list

        


#{ 
 # Driver Code Starts
# Initial Template for Python3


# Node Class
class node:

    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(list1.head)
        printlist(newhead)

# } Driver Code Ends