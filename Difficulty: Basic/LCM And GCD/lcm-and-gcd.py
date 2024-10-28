#User function Template for python3

def gcd(a: int, b: int) -> int:
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a
class Solution:
    def lcmAndGcd(self, a , b):
        # code here 

# def lcmAndGcd(a: int, b: int) -> list:
    # Calculate GCD
        gcd_ab = gcd(a, b)
        
        # Calculate LCM using the formula LCM(a, b) = abs(a * b) / GCD(a, b)
        lcm_ab = abs(a * b) // gcd_ab
    
        return [lcm_ab, gcd_ab]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
        print("~")
# } Driver Code Ends