class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        def is_feasible(mid):
            """Check if it is feasible to allocate books with maximum pages 'mid'."""
            students_required = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages > mid:
                    students_required += 1
                    current_pages = pages
                    if students_required > k:
                        return False
                else:
                    current_pages += pages
            
            return True

        # Edge case: Not enough books for students
        if len(arr) < k:
            return -1

        # Binary search boundaries
        low = max(arr)  # Minimum possible maximum pages
        high = sum(arr)  # Maximum possible maximum pages
        result = -1

        # Binary search
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                result = mid
                high = mid - 1  # Try for a smaller maximum
            else:
                low = mid + 1  # Increase the allowed maximum

        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends