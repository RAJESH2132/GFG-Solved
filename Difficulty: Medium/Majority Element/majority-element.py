#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        count = 0
        element = -1
        n = len(arr)
        for i in range(n):
            if count == 0:
                count = 1
                element = arr[i]
            elif arr[i] == element:
                count += 1
            else:
                count -= 1
        testCount = 0
        for i in arr:
            if i == element:
                testCount += 1
        if testCount > (n//2):
            return element
        else:
            return -1

#User function template for Python 3


        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends