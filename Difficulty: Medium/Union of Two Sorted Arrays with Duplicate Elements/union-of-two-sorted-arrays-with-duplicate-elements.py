class Solution:
    
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        i, j = 0, 0
        union = []
        
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])
                j += 1
        
        # Append remaining elements from array 'a'
        while i < len(a):
            if union[-1] != a[i]:
                union.append(a[i])
            i += 1
        
        # Append remaining elements from array 'b'
        while j < len(b):
            if union[-1] != b[j]:
                union.append(b[j])
            j += 1
        
        return union  # Return outside the while loop


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends