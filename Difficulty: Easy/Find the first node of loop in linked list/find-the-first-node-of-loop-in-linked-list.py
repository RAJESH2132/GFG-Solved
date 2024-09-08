#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
        
       


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, tail, position):
    if position == 0:
        return

    walk = head
    for _ in range(1, position):
        walk = walk.next
    tail.next = walk


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, tail, k)

        ob = Solution()
        ans = ob.findFirstNode(head)
        print(ans)

# } Driver Code Ends