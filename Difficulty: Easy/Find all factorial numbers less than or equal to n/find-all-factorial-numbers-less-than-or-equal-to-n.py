#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        def factorial(current, fact, result):
            if fact > n:
                return
            result.append(fact)
            factorial(current+1, fact*(current+1), result)
        
        result = []
        factorial(1, 1, result)
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
        print("~")

# } Driver Code Ends