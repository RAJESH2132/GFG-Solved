#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        # Get the ith bit
        ith_bit = (num >> (i - 1)) & 1
        
        # Set the ith bit
        num_set_bit = num | (1 << (i - 1))
        
        # Clear the ith bit
        num_clear_bit = num & ~(1 << (i - 1))
        
        # Print the results as space-separated values
        print(ith_bit, num_set_bit, num_clear_bit)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, i = list(map(int, input().split()))
        ob = Solution()
        ob.bitManipulation(n, i)
# } Driver Code Ends