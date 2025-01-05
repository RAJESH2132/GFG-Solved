#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

class Solution:
    def countPairs(self, arr, target):
        # Sort the array
        arr.sort()
        
        # Initialize two pointers and the count of pairs
        left, right = 0, len(arr) - 1
        count = 0
        
        # Use two pointers to find pairs
        while left < right:
            if arr[left] + arr[right] < target:
                # All pairs from left to right-1 are valid
                count += (right - left)
                left += 1
            else:
                # Move the right pointer to reduce the sum
                right -= 1
        
        return count


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends