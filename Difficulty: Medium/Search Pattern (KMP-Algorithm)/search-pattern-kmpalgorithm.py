#User function Template for python3

class Solution:
    def search(self, pat, txt):
        result = []  # List to store the indices of pattern occurrences
        n, m = len(txt), len(pat)  # n is the length of text, m is the length of pattern
        
        # Iterate through the text with a window size equal to the pattern length
        for i in range(n - m + 1):  # Last valid index for the window is n-m
            # Check if the substring matches the pattern
            if txt[i:i + m] == pat:
                result.append(i)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends