#User function Template for python3
class Solution:
	def twoSum(self, nums, target):
		n = len(nums)
        left = 0
        right = n-1
        nums.sort()
        while left < right:
            eleSum = nums[left] + nums[right]
            if eleSum == target:
                return True
            if eleSum < target:
                left += 1
            else:
                right -= 1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends