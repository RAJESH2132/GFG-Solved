#User function template for Python
class Solution:
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
    
        # Step 1: Trim leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
    
        # Step 2: Handle sign
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
    
        # Step 3: Read digits and construct the number
        num = 0
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')  # Convert character to digit
            # Check for overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1
    
        # Step 4: Return the final result with sign
        return sign * num
                    
    

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends