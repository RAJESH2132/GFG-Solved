
#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        i = low
        j = high-1
        
        while i<j:
            while i<high and arr[i]<pivot:
                i+=1
            while j>low and arr[j]>=pivot:
                j-=1
            
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        if arr[i]>pivot:
            arr[i],arr[high] = arr[high],arr[i]
        return i
    
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pi = self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    
        
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends