#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # Initialize variables
        char_set = set()
        max_length = 0
        left = 0
    
        # Iterate through the string with a sliding window
        for right in range(len(s)):
            # If the character is already in the set, remove characters from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
    
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends