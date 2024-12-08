#User function Template for python3
class Solution:
    def missingNumber(self, nums):
        
        n = len(nums)+1
        nSum = n*(n+1)//2

        eleSum = 0
        for i in nums:
            eleSum += i
        
        return nSum-eleSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends