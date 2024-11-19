class Solution:
    def nextPermutation(self,arr):
        n = len(arr)
        ind = -1
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                ind = i
                break
        
        if ind == -1:
            return self.rotated(arr,0,n)
             
        
        for i in range(n-1,-1,-1):
            if arr[i] > arr[ind]:
                arr[i], arr[ind] = arr[ind], arr[i]
                break
            
        return self.rotated(arr,ind+1,n)
        
    def rotated(self,arr,start,end):
        left = start
        right = end-1
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends