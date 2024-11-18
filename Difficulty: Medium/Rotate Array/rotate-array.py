#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        if d > n:
            d = d%n
        self.reverse(arr,0,d)
        self.reverse(arr,d,n)
        self.reverse(arr,0,n)
        return arr
        
    def reverse(self,arr,low,high):
        left = low
        right = high-1
        while left < right:
            arr[left] ,arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends