#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self, s):
        # Code here
        result=[]
        depth=0
        for char in s:
            if char == '(':
                if depth > 0:
                    result.append(char)
                depth+=1
            elif char == ')':
                depth-=1
                if depth>0:
                    result.append(char)
        return ''.join(result)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends