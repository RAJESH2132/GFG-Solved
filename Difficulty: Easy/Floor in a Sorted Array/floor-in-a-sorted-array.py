class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,n,x):
        low, high = 0, len(arr) - 1
        result = -1
    
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                result = mid  # Update result as arr[mid] could be the floor
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half
        
        return result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends