#User function Template for python3
class Solution:
    def oddEven (ob,n):
        # code here 
        if n&1 == 1:
            return "odd"
        else:
            return "even"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.oddEven(N))

# } Driver Code Ends