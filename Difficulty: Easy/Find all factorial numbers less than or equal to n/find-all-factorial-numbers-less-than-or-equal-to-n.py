#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    
        # Initialize an empty list to store the factorial numbers
        factorials = []
        
        def helper(i, current_factorial):
            # Base case: if current factorial exceeds n, stop recursion
            if current_factorial > n:
                return
            
            # Append the current factorial to the list
            factorials.append(current_factorial)
            
            # Recursively calculate the next factorial
            helper(i + 1, current_factorial * (i + 1))
        
        # Start the recursion with i=1 and current factorial as 1 (1! = 1)
        helper(1, 1)
        
        # Return the list of factorial numbers less than or equal to n
        return factorials



    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends