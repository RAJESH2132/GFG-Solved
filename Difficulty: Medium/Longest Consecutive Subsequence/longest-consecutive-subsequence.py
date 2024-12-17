 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr):
        n = len(arr)
        if n == 0:
            return 0
        longest = 0
        st = set()
        for i in arr:
            st.add(i)
        for it in st:
            if it-1 not in st:
                count = 1
                while it+1 in st:
                    count += 1
                    it += 1
                longest = max(longest, count)
        return longest
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a))
        print("~")
# } Driver Code Ends