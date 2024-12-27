#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        store = {}
        count = 0
        
        for num in arr:
            comp = target - num
            # Add the frequency of the complement to the count
            if comp in store:
                count += store[comp]
            # Update the frequency of the current number
            store[num] = store.get(num, 0) + 1
        
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