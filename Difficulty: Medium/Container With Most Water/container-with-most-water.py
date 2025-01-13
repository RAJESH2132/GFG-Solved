
class Solution:
    def maxWater(self, arr):
        # Initialize two pointers
        left = 0
        right = len(arr) - 1
        max_water = 0  # To store the maximum area
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the height and width of the container
            height = min(arr[left], arr[right])
            width = right - left
            
            # Calculate the current area
            current_area = height * width
            
            # Update the maximum area if the current area is larger
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_water


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends