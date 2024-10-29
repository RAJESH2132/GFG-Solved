#User function Template for python3

class Solution:
    def xor_upto(self, n: int) -> int:
        # XOR of numbers from 1 to n depends on n % 4
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0
    
    # def findXOR(self, l: int, r: int) -> int:
        # XOR of range [l, r] is XOR(1, r) ^ XOR(1, l-1)
    
    def findXOR(self, l, r):
        return self.xor_upto(r) ^ self.xor_upto(l - 1)
        # Code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        l, r = list(map(int, input().split()))
        ob = Solution()
        res = ob.findXOR(l, r)
        print(res)
        print("~")
# } Driver Code Ends