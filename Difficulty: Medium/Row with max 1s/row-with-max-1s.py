class Solution:
    
    def lowerBound(self,arr,n,x):
        low = 0
        high = n-1
        ans = n
    
        while low<=high:
            mid = low + (high-low)//2
    
            if arr[mid] >= x:
                ans = mid
                high = mid-1
            else:
                low  = mid+1
        return ans
    
    
    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])
        count_max = 0
        index = -1
    
        for i in range(n):
    
            count_ones = m - self.lowerBound(mat[i],m,1)
            if count_ones > count_max:
                count_max = count_ones
                index = i
        return index






#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    tc = int(data[idx])
    idx += 1
    results = []

    for _ in range(tc):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        ans = Solution().rowWithMax1s(arr)
        results.append(ans)

    for result in results:
        print(result)

# } Driver Code Ends