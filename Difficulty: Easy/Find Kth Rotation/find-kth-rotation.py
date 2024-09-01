#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low = 0
        high = n-1
    
        while low < high:
            mid = low + (high-low)//2
    
            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid+1
        return low



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)

# } Driver Code Ends