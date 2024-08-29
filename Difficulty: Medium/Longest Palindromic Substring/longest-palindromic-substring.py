#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
      
        if not S:
            return ""

        def expand_around_center(s: str, left: int, right: int) -> (int, int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the indices of the start and end of the palindrome
            return (left + 1, right - 1)
        
        start = 0
        end = 0

        for i in range(len(S)):
            # Check for odd length palindromes
            left1, right1 = expand_around_center(S, i, i)
            # Check for even length palindromes
            left2, right2 = expand_around_center(S, i, i + 1)

            # Choose the longer palindrome
            if right1 - left1 > right2 - left2:
                new_start, new_end = left1, right1
            else:
                new_start, new_end = left2, right2

            # Update the start and end indices if a longer palindrome is found
            if new_end - new_start > end - start:
                start, end = new_start, new_end

        return S[start:end + 1]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends