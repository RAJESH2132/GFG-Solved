#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        if N <1:
            return -1
        if N==1 and arr[0]!=K:
            return -1
    
        if N>1:
            x=N//2
            if K>arr[x]:
                for i in range(x+1,N):
                    if arr[i]==K:
                        return 1
            elif arr[x]==K:
                return 1
            else:
                for i in range(0,x):
                    if arr[i]==K:
                        return 1
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends