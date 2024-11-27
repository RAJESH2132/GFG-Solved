#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        # Step 1: Filter only positive numbers and create a set
        positive_numbers = set(num for num in arr if num > 0)
    
        # Step 2: Check for the smallest missing positive starting from 1
        smallest = 1
        while smallest in positive_numbers:
            smallest += 1
    
        return smallest


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends