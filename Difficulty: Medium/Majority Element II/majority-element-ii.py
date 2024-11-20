class Solution:
    def findMajority(self, arr):
        n = len(arr)
        # Step 1: Finding potential majority elements
        cnt1, cnt2, ele1, ele2 = 0, 0, None, None
        
        for num in arr:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1, cnt1 = num, 1
            elif cnt2 == 0:
                ele2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Step 2: Verifying the candidates
        cnt1, cnt2 = 0, 0
        for num in arr:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1

        # Step 3: Collecting the majority elements
        result = []
        threshold = n // 3  # An element must appear more than n/3 times to be a majority
        if cnt1 > threshold:
            result.append(ele1)
        if cnt2 > threshold:
            result.append(ele2)

        result.sort()  # Optional, if sorted output is needed
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends