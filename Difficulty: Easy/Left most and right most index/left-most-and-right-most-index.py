#User function Template for python3

class Solution:
    def indexes(self, nums, target):

        # Function to find the first occurrence of the target
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first_occurrence = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    high = mid - 1  # Keep searching to the left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return first_occurrence
        
        # Function to find the last occurrence of the target
        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last_occurrence = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    low = mid + 1  # Keep searching to the right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return last_occurrence
        
        # Call the helper functions to get the first and last occurrence
        first_occurrence = findFirst(nums, target)
        last_occurrence = findLast(nums, target)
        
        return [first_occurrence, last_occurrence]

        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends