#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        mapStr1 = {}
        mapStr2 = {}
        if len(str1)==0 or len(str2)==0 or len(str1)!=len(str2):
            return 0
        for c1,c2 in zip(str1,str2):
            if (c1 in mapStr1 and mapStr1[c1]!=c2) or (c2 in mapStr2 and mapStr2[c2]!=c1):
                return 0
            mapStr1[c1] = c2
            mapStr2[c2] = c1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends