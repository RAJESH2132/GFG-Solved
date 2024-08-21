#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        preSum = {}
        maxLen = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == k:
                maxLen = max(maxLen,i+1)
            rem = sum-k
            if rem in preSum:
                length = i - preSum[rem]
                maxLen = max(maxLen,length)
            if sum not in preSum:
                preSum[sum] = i
        return maxLen
                
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends