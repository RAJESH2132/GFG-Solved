#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        maxSum = 0
        n = len(arr)

        # Iterate through adjacent pairs
        for i in range(n - 1):
            # Compute the sum of the current pair
            currentSum = arr[i] + arr[i + 1]
            # Update maxSum if currentSum is greater
            maxSum = max(maxSum, currentSum)

        return maxSum
                
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends