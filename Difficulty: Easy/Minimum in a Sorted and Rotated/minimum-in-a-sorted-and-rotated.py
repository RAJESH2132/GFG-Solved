#User function Template for python3

class Solution:
    def findMin(self, arr):
        n = len(arr)
        low = 0
        high = n-1
        
        while low < high:
            mid = low + (high-low)//2
            
            if arr[mid]<arr[high]:
                high = mid
            else:
                low = mid+1
        return arr[low]


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends