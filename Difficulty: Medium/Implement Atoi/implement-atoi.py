#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        
        # Handle the case where the string is empty
        if len(s) == 0:
            return -1
        
        # Check if the string starts with a '-' and the rest are digits
        if s[0] == '-' and s[1:].isdigit():
            num = 0
            for char in s[1:]:
                num = num * 10 + (ord(char) - ord('0'))
            return -num
        
        # Check if all characters in the string are digits
        elif s.isdigit():
            num = 0
            for char in s:
                num = num * 10 + (ord(char) - ord('0'))
            return num
        
        # If the string cannot be converted to an integer
        return -1
                
            


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends