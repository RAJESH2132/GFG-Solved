class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        leaders_list = []
        
        # Start with the rightmost element as the first leader
        max_from_right = arr[-1]
        leaders_list.append(max_from_right)
        
        # Traverse the array from the second last element to the left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders_list.append(arr[i])
                max_from_right = arr[i]
        
        # Since we collected leaders in reverse order, reverse the list before returning
        leaders_list.reverse()
        
        return leaders_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends