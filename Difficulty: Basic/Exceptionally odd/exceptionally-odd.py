#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        xor = 0
        for ele in arr:
            xor ^= ele
        return xor


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends