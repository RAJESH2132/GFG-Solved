#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        low, high = max(0, k - n), min(k, m)

        while low <= high:
            cut1 = (low + high) // 2  # Partition `a`
            cut2 = k - cut1          # Partition `b`

            # Use negative and positive infinity for boundary conditions
            left1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            left2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            right1 = a[cut1] if cut1 < m else float('inf')
            right2 = b[cut2] if cut2 < n else float('inf')

            # Valid partition found
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)

            # Adjust binary search range
            if left1 > right2:
                high = cut1 - 1  # Move left in `a`
            else:
                low = cut1 + 1   # Move right in `a`

        return -1  # Should not reach here
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends