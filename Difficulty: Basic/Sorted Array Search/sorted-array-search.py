#User function Template for python3

class Solution:
    def searchInSorted(self, arr, K):
        # Binary Search Algorithm
        N = len(arr)
        left, right = 0, N - 1
        
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # Check if the middle element is the target
            if arr[mid] == K:
                return True
            # If the target is greater, ignore the left half
            elif arr[mid] < K:
                left = mid + 1
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # Target not found
        return False






#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends