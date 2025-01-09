#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        left = 0
        current_sum = 0
    
        for right in range(len(arr)):
            current_sum += arr[right]
    
            # Shrink the window if the current sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
    
            # Check if we found the subarray with the required sum
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based indexing
    
        # If no subarray is found
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends