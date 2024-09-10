#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if head is None or head.next is None:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next if head.next else None

        # Move 'fast' pointer twice as fast as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head



#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        obj = Solution()
        res = obj.deleteMid(head)
        printList(res)

# } Driver Code Ends