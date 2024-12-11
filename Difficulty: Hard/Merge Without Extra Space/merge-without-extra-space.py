import math
class Solution:
    def mergeArrays(self, a, b):

        n, m = len(a), len(b)
        gap = math.ceil((n + m) / 2)  # Initial gap size
    
        while gap > 0:
            i = 0
    
            # Compare elements in the first array
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                i += 1
    
            # Compare elements between both arrays
            j = max(0, gap - n)
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
    
            # Compare elements in the second array
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1
    
            # Reduce the gap size
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap / 2)
        
#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends