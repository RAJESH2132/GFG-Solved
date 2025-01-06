class Solution:
    def sumClosest(self, arr, target):
        # Edge case: If the array has less than two elements, return an empty array
        if len(arr) < 2:
            return []
        
        # Sort the array to enable two-pointer approach
        arr.sort()
        
        # Initialize variables
        closest_pair = []
        closest_diff = float('inf')
        max_abs_diff = float('-inf')
        
        # Two-pointer approach
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = abs(current_sum - target)
            
            if current_diff < closest_diff or (current_diff == closest_diff and abs(arr[right] - arr[left]) > max_abs_diff):
                # Update the closest pair, difference, and max absolute difference
                closest_pair = [arr[left], arr[right]]
                closest_diff = current_diff
                max_abs_diff = abs(arr[right] - arr[left])
            
            # Move the pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If we find an exact match, return the pair
                return [arr[left], arr[right]]
        
        return closest_pair



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends