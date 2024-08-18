#User function Template for python3

class Solution:
    def searchInSorted(self, arr, N, K):
        # Binary Search Algorithm
        left, right = 0, N - 1
        
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # Check if the middle element is the target
            if arr[mid] == K:
                return 1
            # If the target is greater, ignore the left half
            elif arr[mid] < K:
                left = mid + 1
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # Target not found
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends