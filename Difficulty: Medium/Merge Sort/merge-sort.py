#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def merge(self, array, start, middle, end):
        merged = []
        left_index = start
        right_index = middle+1
        
        while left_index <= middle and right_index <= end:
            if array[left_index] <= array[right_index]:
                merged.append(array[left_index])
                left_index += 1
            else:
                merged.append(array[right_index])
                right_index += 1
                
        while left_index <= middle:
            merged.append(array[left_index])
            left_index += 1
        
        while right_index <= end:
            merged.append(array[right_index])
            right_index += 1
        
        for i in range(start, end+1):
            array[i] = merged[i-start]
    
    def mergeSort(self,array, start, end):
        if start >= end:
            return
        
        middle = (start+end)//2
        self.mergeSort(array, start, middle)
        self.mergeSort(array, middle+1, end)
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