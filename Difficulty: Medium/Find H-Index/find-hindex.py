#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1) (if we ignore the input storage for sorting)
        """
        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)
        
        # Step 2: Find the maximum H-index
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:  # Check if the current citation supports H = i + 1
                h_index = i + 1
            else:
                break
        
        return h_index


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends