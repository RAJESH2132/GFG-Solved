#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        n = len(arr)
        if n < 2:
            return -1
        large = float("-inf")
        second_largest= float("-inf")
        repeating = True
        for i in range(n):
            if arr[i]>large:
                second_largest = large
                large = arr[i]
            elif (arr[i]>second_largest) and (arr[i]!=large):
                second_largest = arr[i]
            if i<n-1 and (arr[i]!=arr[i+1]) :
                repeating = False
        return -1 if repeating else second_largest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends