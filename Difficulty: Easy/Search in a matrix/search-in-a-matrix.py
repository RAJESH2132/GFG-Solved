class Solution:

	#Function to check if element x is present in the matrix.
	def matSearch(self,mat, n, m, x):
		
		i = 0
		j = m-1
		
		#iterating through the matrix
		while i < n and j >= 0:

			#if the current element is equal to x, return 1
			if mat[i][j] == x:
				return 1

			#if the current element is greater than x, move left
			if mat[i][j] > x:
				j -= 1

			#if the current element is less than x, move down
			else:  
				i += 1

		#if x is not found in the matrix, return 0
		return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends