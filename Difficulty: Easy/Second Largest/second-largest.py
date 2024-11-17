class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second_largest = -1
        
        for e in arr:
            if e > largest:  
                second_largest = largest
                largest = e
            elif largest > e > second_largest:
                second_largest = e
        
        return second_largest
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends