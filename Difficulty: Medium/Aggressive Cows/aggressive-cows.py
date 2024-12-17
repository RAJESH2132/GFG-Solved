class Solution:
    def aggressiveCows(self, stalls, k):
        # Sort the stall positions
        stalls.sort()
        
        def can_place_cows(distance):
            # Place the first cow in the first stall
            count, last_position = 1, stalls[0]
            
            # Try placing the rest of the cows
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                    if count == k:  # All cows placed
                        return True
            return False
        
        # Binary search for the largest minimum distance
        low, high = 1, stalls[-1] - stalls[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place_cows(mid):
                result = mid  # Update result
                low = mid + 1  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends