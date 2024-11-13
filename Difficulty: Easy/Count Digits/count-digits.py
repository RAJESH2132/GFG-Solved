#User function Template for python3


class Solution:
    def evenlyDivides (self, n):
        count = 0
        original = n
        while n > 0:
            digit = n % 10
            if digit != 0 and original % digit == 0:
                count += 1
            n = n //10
        return count








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends