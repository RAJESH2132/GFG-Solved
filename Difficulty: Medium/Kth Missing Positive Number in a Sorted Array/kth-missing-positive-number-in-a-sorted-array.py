class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        
        # Binary search to find the position
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # Missing numbers up to index `mid`
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # `left` is now the position where the kth missing lies
        # Calculate the kth missing number
        return left + k




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends