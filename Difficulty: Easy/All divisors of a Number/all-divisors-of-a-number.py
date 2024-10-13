#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def print_divisors(self, n):
        arr = []
        i = 1
        while i*i<=n:
            if n%i==0:
                arr.append(i)
                if n/i != i:
                    arr.append(n//i)
            i+=1
        arr.sort()
        for i in arr:
            print(i,end=' ')
        
        
        


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends