#User function Template for python3

class Solution:
    def findSubArraySum(self, arr, n, k):
        # code here
        dictt = {0:1}
        preSum = 0
        count = 0
        dictt[0] = 1
        for num in arr:
            preSum += num
            remove = preSum-k
            if remove in dictt:
                count += dictt[remove]
            if preSum in dictt:
                dictt[preSum] += 1
            else:
                dictt[preSum] = 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends