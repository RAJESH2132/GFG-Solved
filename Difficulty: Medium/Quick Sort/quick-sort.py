class Solution:
    
    def quickSort(self,arr,low,high):
        if low < high:
            partitionIndex = self.partition(arr,low,high)
            
            self.quickSort(arr, low, partitionIndex-1)
            self.quickSort(arr, partitionIndex+1, high)
            
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1
            while j >= low + 1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        print("~")

# } Driver Code Ends