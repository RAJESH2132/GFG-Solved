#User function Template for python3
class Solution:
    def firstOccurence(self,arr,n,x):
        first = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid]==x:
                first = mid
                high = mid-1
            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1
        return first
    
    def lastOccurence(self,arr,n,x):
        last = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid]==x:
                last = mid
                low = mid+1
            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1
        return last
        
    
    def firstAndLastPosition(self,arr,n,x):
        first = self.firstOccurence(arr,n,x)
        last = self.lastOccurence(arr,n,x)
        if first == -1:
            return (-1,-1)
        return (first,last)
        
	def count(self,arr, n, x):
	    first , last = self.firstAndLastPosition(arr,n,x)
	    if first == -1:
	        return 0
	    return last-first+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends