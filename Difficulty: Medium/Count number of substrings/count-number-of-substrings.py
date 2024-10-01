#User function Template for python3
from collections import defaultdict
class Solution:
    def substrCount(self, s: str, k: int) -> int:
        # Helper function to count substrings with at most k distinct characters
        def countAtMostKDistinct(s, k):
            count = 0
            left = 0
            freq_map = defaultdict(int)
            
            for right in range(len(s)):
                freq_map[s[right]] += 1
                
                # If we have more than k distinct characters, shrink the window
                while len(freq_map) > k:
                    freq_map[s[left]] -= 1
                    if freq_map[s[left]] == 0:
                        del freq_map[s[left]]
                    left += 1
                
                # Number of substrings with at most k distinct characters
                count += right - left + 1
            
            return count
        
        # Number of substrings with exactly k distinct characters
        return countAtMostKDistinct(s, k) - countAtMostKDistinct(s, k - 1)






#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends