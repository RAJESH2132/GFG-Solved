class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        minPrice = prices[0]
        profit = 0
        for i in range(1,n):
            minPrice = min(minPrice,prices[i])
            profit = max(profit,prices[i]-minPrice)
        if profit < 0:
            return 0
        return profit

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends