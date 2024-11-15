class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,x):
        n = len(arr)
        low, high = 0, len(arr) - 1
        result = -1
    
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                result = mid  # Update result as arr[mid] could be the floor
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half
        
        return result
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends