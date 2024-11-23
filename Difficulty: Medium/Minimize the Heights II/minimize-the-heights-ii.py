#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        n = len(arr)
        # Step 1: Sort the array
        arr.sort()

        # Initial difference (before any modification)
        min_diff = arr[-1] - arr[0]

        # Smallest and largest after modifications
        smallest = arr[0] + k
        largest = arr[-1] - k

        # Ensure smallest is always less than or equal to largest
        if smallest > largest:
            smallest, largest = largest, smallest

        # Step 2: Traverse the array to find the minimum difference
        for i in range(1, n):
            if arr[i] - k < 0:  # Skip if height becomes negative
                continue

            min_after = min(smallest, arr[i] - k)  # Minimum of current configuration
            max_after = max(largest, arr[i - 1] + k)  # Maximum of current configuration

            # Update the minimum difference
            min_diff = min(min_diff, max_after - min_after)

        return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends