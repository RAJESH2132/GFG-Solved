#User function Template for python3

class Solution:
    def search(self,arr,target):
        n = len(arr)
        low = 0
        high = n-1

        while low <= high:
            mid = low + (high-low)//2

            if arr[mid] == target:
                return mid
            
            if arr[low] <= arr[mid]:
                if arr[low] <= target <= arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if arr[mid] <= target <= arr[high]:
                    low = mid+1
                else:
                    high = mid -1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends