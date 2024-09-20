#User function Template for python3

class Solution:
	def AllPrimeFactors(self, n):
	    prime_factors = []

        # Check for number of 2s
        if n % 2 == 0:
            prime_factors.append(2)
        while n % 2 == 0:
            n //= 2
        
        # Check for odd numbers till √n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                prime_factors.append(i)
            while n % i == 0:
                n //= i
    
        # If n is still a prime number greater than 2
        if n > 2:
            prime_factors.append(n)
        
        return prime_factors

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends