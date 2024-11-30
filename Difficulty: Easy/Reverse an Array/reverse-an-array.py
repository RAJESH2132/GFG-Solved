class Solution:
    def reverseArray(self, arr):
        def reverse_helper(arr, start, end):
            # Base case: If pointers meet or cross, stop recursion
            if start >= end:
                return
            # Swap elements at start and end
            arr[start], arr[end] = arr[end], arr[start]
            # Recurse for the remaining array
            reverse_helper(arr, start + 1, end - 1)

        # Call the helper function with full array
        reverse_helper(arr, 0, len(arr) - 1)
        return arr
        
        
        


#{ 
 # Driver Code Starts
import sys


def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())

    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()

        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]

        # Create a Solution object
        obj = Solution()

        # Reverse the array
        obj.reverseArray(arr)

        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")

        # Decrement the test case count
        tc -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends