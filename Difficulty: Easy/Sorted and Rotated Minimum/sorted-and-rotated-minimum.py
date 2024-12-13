class Solution:
    def findMin(self, arr):
        """
        Find the minimum element in a rotated sorted array.
        
        Time Complexity: O(log n) - Binary search is used.
        Space Complexity: O(1) - Constant space is used.
        """
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the high element,
            # the minimum is in the right half.
            if arr[mid] > arr[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                high = mid
        
        # After the loop, low == high and points to the minimum element.
        return arr[low]


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends