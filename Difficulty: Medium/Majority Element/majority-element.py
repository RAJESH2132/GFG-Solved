#User function template for Python 3

class Solution:
    def majorityElement(self, arr, n):
        count = 0
        element = 0
        for i in range(n):
            if count == 0:
                element = arr[i]
                count = 1
            elif arr[i] == element:
                count+=1
            else:
                count -= 1
        
        count1 = 0
        for i in range(n):
            if arr[i]==element:
                count1+=1
        if count1 > (n/2):
            return element
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends