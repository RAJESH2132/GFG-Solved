#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,num):
        count = 0
        # Traverse all bit positions (up to 31 for a 32-bit integer)
        for bit_pos in range(32):
            # Compute groups of 'full cycles' of 0s and 1s for the current bit position
            complete_groups = (num + 1) // (1 << (bit_pos + 1))
            remainder = (num + 1) % (1 << (bit_pos + 1))
            
            # Add to count based on full groups
            count += complete_groups * (1 << bit_pos)
            
            # Add extra set bits in the last incomplete group (if any)
            if remainder > (1 << bit_pos):
                count += remainder - (1 << bit_pos)
        
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends