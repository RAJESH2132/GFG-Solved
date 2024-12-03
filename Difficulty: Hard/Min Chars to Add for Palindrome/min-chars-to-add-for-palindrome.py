class Solution:
    def minChar(self, s: str) -> int:
        # Step 1: Construct the temporary string
        temp = s + "#" + s[::-1]

        # Step 2: Compute the LPS (Longest Prefix Suffix) array
        n = len(temp)
        lps = [0] * n  # Initialize LPS array
        i, j = 1, 0    # Start with the second character
        
        while i < n:
            if temp[i] == temp[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # Step 3: Calculate the minimum characters to add
        min_chars = len(s) - lps[-1]
        return min_chars


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends