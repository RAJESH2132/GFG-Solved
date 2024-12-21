class Solution:
    
    # Function to rotate matrix clockwise by 90 degrees.
    def rotateby90(self, a):
        n = len(a)
        # Finding transpose of the matrix
        for row in range(n):
            for col in range(row + 1, n):
                a[row][col], a[col][row] = a[col][row], a[row][col]

        # Reverse every column
        for col in range(n):
            start, end = 0, n - 1
            while start < end:
                a[start][col], a[end][col] = a[end][col], a[start][col]
                start += 1
                end -= 1

        return a



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.rotateby90(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

        print("~")

# } Driver Code Ends