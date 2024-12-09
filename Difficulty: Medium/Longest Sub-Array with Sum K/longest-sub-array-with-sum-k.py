class Solution:
    def lenOfLongestSubarr(self, a, k):  
        n = len(a)  # Size of the array

        preSumMap = {}  # Hash map to store prefix sums
        Sum = 0  # Running prefix sum
        maxLen = 0  # Maximum length of subarray with sum `k`

        for i in range(n):
        # Calculate the prefix sum till index `i`
            Sum += a[i]

        # If the prefix sum equals `k`, update the maximum length
            if Sum == k:
                maxLen = max(maxLen, i + 1)

        # Calculate the remaining sum needed to reach `k`
            rem = Sum - k

        # If the remaining sum exists, calculate the subarray length
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)

        # If the prefix sum is not in the map, store it
            if Sum not in preSumMap:
                preSumMap[Sum] = i

        return maxLen

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends