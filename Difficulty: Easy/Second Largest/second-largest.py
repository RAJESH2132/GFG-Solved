#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest = arr[0]
        second_largest = -1
        for ele in arr:
            if ele > largest:
                second_largest = largest
                largest = ele
            if ele < largest and ele > second_largest:
                second_largest = ele
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