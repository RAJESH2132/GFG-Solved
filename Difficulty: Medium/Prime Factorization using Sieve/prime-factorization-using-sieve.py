#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# class Solution:
#     def sieve(self):
        
#     def findPrimeFactors(self, N):
        
class Solution:
    def sieve(self, max_n=2 * 10**5):
        # Initialize SPF array (smallest prime factor) for each number up to max_n
        self.spf = list(range(max_n + 1))  # spf[i] will be initialized to i
        
        # Start Sieve of Eratosthenes for finding the smallest prime factors
        for i in range(2, int(max_n**0.5) + 1):
            if self.spf[i] == i:  # i is a prime
                # Mark multiples of i with i as the smallest prime factor
                for j in range(i * i, max_n + 1, i):
                    if self.spf[j] == j:  # Mark j only if it hasn't been marked yet
                        self.spf[j] = i

    def findPrimeFactors(self, N):
        # Precompute SPF for all numbers up to the size of N
        # List to store prime factors of N
        prime_factors = []
        
        # Using the precomputed SPF array to find prime factors of N
        while N > 1:
            prime_factors.append(self.spf[N])
            N //= self.spf[N]
        
        return prime_factors
        



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    ob = Solution()
    ob.sieve()
    for _ in range (t):
        n = int(input())
        ans = ob.findPrimeFactors(n)
        for v in ans:
            print(v, end = ' ')
        print()
# } Driver Code Ends