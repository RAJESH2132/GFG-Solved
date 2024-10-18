#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        # Helper recursive function to generate factorial numbers <= n
        def factorial_helper(i, fact, n, result):
            # Base case: if factorial exceeds n, stop recursion
            if fact > n:
                return
            
            # Append the current factorial to the result list
            result.append(fact)
            
            # Recursive case: calculate the next factorial (i+1)! and continue
            factorial_helper(i + 1, fact * (i + 1), n, result)

        # Initialize the result list and start recursion from 1! = 1
        result = []
        factorial_helper(1, 1, n, result)
        return result
    	


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