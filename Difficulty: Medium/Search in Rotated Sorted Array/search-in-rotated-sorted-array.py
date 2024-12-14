#User function Template for python3

class Solution:
    def search(self,arr,key):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            # Check if mid is the target
            if arr[mid] == key:
                return mid

            # Check if the left half is sorted
            if arr[start] <= arr[mid]:
                # If key lies in the sorted left half
                if arr[start] <= key < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # If the right half is sorted
                if arr[mid] < key <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends