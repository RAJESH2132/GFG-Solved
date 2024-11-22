#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:
    
    def merge(self, arr, low, mid, high):
        # Temporary array
        temp = []
        left = low       # Starting index of left half of arr
        right = mid + 1  # Starting index of right half of arr
        
        # Merging two halves in a sorted manner
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        # Adding remaining elements from the left half
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        # Adding remaining elements from the right half
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # Copy sorted elements back to the original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        
    def mergeSort(self, arr, left, right):
        # Safeguards against invalid inputs
        if len(arr) == 0 or left < 0 or right >= len(arr) or left >= right:
            return
        
        mid = (left + right) // 2
        # Recursively sort the left and right halves
        self.mergeSort(arr, left, mid)  # Left half
        self.mergeSort(arr, mid + 1, right)  # Right half
        # Merge the sorted halves
        self.merge(arr, left, mid, right)



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends