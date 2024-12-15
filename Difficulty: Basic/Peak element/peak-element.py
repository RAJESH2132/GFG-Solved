
class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            # Compare middle element with its neighbor
            if arr[mid] > arr[mid + 1]:
                # Mid might be a peak or peak lies to the left
                right = mid
            else:
                # Peak lies to the right
                left = mid + 1

        # Left and right converge to a peak index
        return left



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends