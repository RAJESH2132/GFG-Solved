#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        
        unique = 0
        for i in range(1,len(arr)):
            if arr[i] != arr[unique]:
                unique += 1
                arr[unique] = arr[i]
        return unique+1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends