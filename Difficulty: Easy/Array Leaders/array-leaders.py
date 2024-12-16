class Solution:
    def leaders(self, arr):
        leaders = []
        great = arr[-1]
        n = len(arr)
        leaders.append(arr[-1])
        for i in range(n-2,-1,-1):
            if  arr[i] >= great:
                leaders.append(arr[i])
                great = arr[i]
        return reversed(leaders)
            
#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends