#User function Template for python3
class Solution:
    def search(self, n, arr):
        left = 0
        right = n-1
        
        while left != right:
            mid = left + (right-left)//2
            
            if mid%2 == 1:
                mid -= 1
            
            if arr[mid] == arr[mid+1]:
                left = mid+2
                
            else:
                right = mid
        return arr[left]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(n, arr))

# } Driver Code Ends