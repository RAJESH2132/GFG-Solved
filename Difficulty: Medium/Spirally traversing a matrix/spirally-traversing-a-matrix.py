class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m-1
        top = 0
        bottom = n-1
        ans = []

        while (top <= bottom and left <= right):

            # Right Direction (Left --> Right)
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            # Bottom Direction (right side top --> Bottom)
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            # left Direction (bottom right --> left)
            if (top <= bottom):
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Top Direction (left side Bottom --> Top)
            if (left <= right):
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


#{ 
 # Driver Code Starts
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

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends