#User function Template for python3

class Solution:
    def printGfg(self, N):
    
        # Base case: If N is less than or equal to 0, return (do nothing)
        if N <= 0:
            return
        # Print "GFG" followed by a space
        print("GFG", end=' ')
        # Recursive call with N-1
        self.printGfg(N - 1)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
# } Driver Code Ends