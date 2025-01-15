# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # Dictionary to store the first occurrence of a cumulative sum
        prefix_sum_map = {}
        # Initialize variables
        current_sum = 0
        max_length = 0
    
        for i, num in enumerate(arr):
            # Add current number to the cumulative sum
            current_sum += num
    
            # Check if the current cumulative sum is equal to k
            if current_sum == k:
                max_length = max(max_length, i + 1)
    
            # If the difference (current_sum - k) exists in the map, update max_length
            if current_sum - k in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[current_sum - k])
    
            # If current_sum is not already in the map, store it with the current index
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i
    
        return max_length
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends