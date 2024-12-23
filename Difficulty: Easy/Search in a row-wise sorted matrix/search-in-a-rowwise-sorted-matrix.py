class Solution:
    
    # Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x):
        
        def binarySearch(arr, x):
            
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                
                # If x == arr[mid], return True
                if x == arr[mid]:
                    return True
                
                # If x < arr[mid], search in the left half
                if x < arr[mid]:
                    hi = mid - 1
                
                # If x > arr[mid], search in the right half
                else:
                    lo = mid + 1
            return False

        # Number of rows and columns in the matrix
        n, m = len(mat), len(mat[0])
        
        # Iterate over all rows to find x
        for i in range(n):
            
            # Perform binary search on the ith row
            if binarySearch(mat[i], x):
                return True
        
        # If x was not found, return False
        return False

    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends