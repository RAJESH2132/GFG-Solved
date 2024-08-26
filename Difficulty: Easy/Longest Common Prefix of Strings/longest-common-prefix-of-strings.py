#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # If the array is empty, return an empty string
        if not arr:
            return ""

        # If the array has only one string, return that string
        if len(arr) == 1:
            return arr[0]

        # Sort the array to bring similar strings closer
        arr.sort()

        # Get the first and last strings from the sorted array
        first = arr[0]
        last = arr[-1]

        # Find the common prefix between the first and last strings
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        # The common prefix is the substring from the start to index 'i'
        common_prefix = first[:i]

        # If there's no common prefix, return "-1", otherwise return the prefix
        return "-1" if not common_prefix else common_prefix



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends