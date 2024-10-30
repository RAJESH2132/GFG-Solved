#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        xor_all = 0
        
        # XOR all elements to get xor_all (which will be the XOR of the two odd occurring numbers)
        for num in Arr:
            xor_all ^= num
        
        # Find the rightmost set bit in xor_all (which is different in the two odd occurring numbers)
        rightmost_set_bit = xor_all & -xor_all
        
        # Divide numbers into two groups based on the rightmost set bit
        x = 0
        y = 0
        
        for num in Arr:
            if num & rightmost_set_bit:
                x ^= num  # Numbers with the set bit
            else:
                y ^= num  # Numbers without the set bit
        
        # Return the two odd occurring numbers in decreasing order
        return sorted([x, y], reverse=True)






#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
        print("~")
# } Driver Code Ends