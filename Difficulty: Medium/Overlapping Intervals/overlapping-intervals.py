class Solution:
	def mergeOverlap(self, intervals):
		# Step 1: Sort intervals by their starting point
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize result list with the first interval
        merged = []
        for interval in intervals:
            # If merged list is empty or no overlap with the last interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # Add the interval to the result
            else:
                # Overlapping intervals, merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends