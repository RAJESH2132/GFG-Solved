#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:

    def merge(self, array, start, middle, end):
        """
        Merges two sorted subarrays of 'array' into a single sorted subarray.
        Subarray 1: array[start:middle+1]
        Subarray 2: array[middle+1:end+1]
        """

        # Temporary array to store merged elements
        merged = []
        
        # Indices for left and right subarrays
        left_index = start     # Starting index of the left subarray
        right_index = middle + 1  # Starting index of the right subarray

        # Compare elements from both subarrays and merge them in sorted order
        while left_index <= middle and right_index <= end:
            if array[left_index] <= array[right_index]:
                merged.append(array[left_index])
                left_index += 1
            else:
                merged.append(array[right_index])
                right_index += 1

        # Append remaining elements from the left subarray (if any)
        while left_index <= middle:
            merged.append(array[left_index])
            left_index += 1

        # Append remaining elements from the right subarray (if any)
        while right_index <= end:
            merged.append(array[right_index])
            right_index += 1

        # Copy the merged elements back into the original array
        for i in range(start, end + 1):
            array[i] = merged[i - start]

    def mergeSort(self, array, start, end):
        """
        Recursively divides the array into smaller subarrays and sorts them.
        Then merges the sorted subarrays to form the final sorted array.
        """

        # Base condition: If the subarray has one or no elements, it's already sorted
        if start >= end:
            return

        # Calculate the middle index of the current subarray
        middle = (start + end) // 2

        # Recursively sort the left half
        self.mergeSort(array, start, middle)

        # Recursively sort the right half
        self.mergeSort(array, middle + 1, end)

        # Merge the sorted halves
        self.merge(array, start, middle, end)





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