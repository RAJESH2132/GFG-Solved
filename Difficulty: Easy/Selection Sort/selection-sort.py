#User function Template for python3

class Solution: 

    def selectionSort(self, arr,n):
        for i in range(n-1):
            mini = i
            for j in range(i+1,n):
                if (arr[j]<arr[mini]):
                    mini = j
            arr[i] , arr[mini] = arr[mini] , arr[i]
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
        print("~")
# } Driver Code Ends