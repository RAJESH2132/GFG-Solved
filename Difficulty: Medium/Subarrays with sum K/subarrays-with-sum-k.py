#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        prefix_sum_count = {0: 1}  # Dictionary to store frequency of prefix sums
        count = 0
        current_prefix_sum = 0
    
        for num in arr:
            current_prefix_sum += num
            needed_prefix_sum = current_prefix_sum - k
            
            if needed_prefix_sum in prefix_sum_count:
                count += prefix_sum_count[needed_prefix_sum]
            
            if current_prefix_sum in prefix_sum_count:
                prefix_sum_count[current_prefix_sum] += 1
            else:
                prefix_sum_count[current_prefix_sum] = 1
    
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends