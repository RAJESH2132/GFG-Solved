# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)  # Calculate the total sum of the array
        left_sum = 0          # Initialize the left sum as 0
    
        for i, num in enumerate(arr):
            # Calculate the right sum as total_sum - left_sum - current element
            right_sum = total_sum - left_sum - num
    
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
    
            # Update the left sum by adding the current element
            left_sum += num
    
        return -1







#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends