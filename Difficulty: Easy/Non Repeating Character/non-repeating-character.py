'''
Time Complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        n = len(s)
        arr = [0] * 26  # Size 26 for each letter of the alphabet.
        
        # Step 1: Count the frequency of each character
        for i in s:
            index = ord(i) - ord('a')
            arr[index] += 1
        
        # Step 2: Find the first non-repeating character
        for i in range(n):
            index = ord(s[i]) - ord('a')
            if arr[index] == 1:
                return s[i]  # Return the first non-repeating character
        
        return -1  # If no non-repeating character is found


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
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")

# } Driver Code Ends