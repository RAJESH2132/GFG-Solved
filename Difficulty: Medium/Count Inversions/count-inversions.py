class Solution:
    def inversionCount(self, arr):
        """
        Function to count inversions using merge sort.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        n = len(arr)
        return self.mergeSort(arr, 0, n - 1)
    
    def mergeSort(self, arr, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        inversions = 0
        
        # Count inversions in left and right halves
        inversions += self.mergeSort(arr, left, mid)
        inversions += self.mergeSort(arr, mid + 1, right)
        
        # Count inversions during merge
        inversions += self.merge(arr, left, mid, right)
        return inversions
    
    def merge(self, arr, left, mid, right):
        # Temporary arrays for merging
        leftArr = arr[left:mid + 1]
        rightArr = arr[mid + 1:right + 1]
        
        i, j, k = 0, 0, left
        inversions = 0
        
        # Merge while counting inversions
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                inversions += (mid + 1 - (left + i))  # Count inversions
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
        
        return inversions



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
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends