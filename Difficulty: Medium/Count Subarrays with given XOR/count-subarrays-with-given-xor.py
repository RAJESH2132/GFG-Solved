class Solution:
    def subarrayXor(self, arr, k):
        freq = {}
        current_xor = 0
        count = 0
    
        for num in arr:
            # Update the current XOR
            current_xor ^= num
    
            # Check if current XOR is equal to k
            if current_xor == k:
                count += 1
    
            # Check if there exists a prefix XOR such that 
            # current_xor ^ prefix_xor = k
            if (current_xor ^ k) in freq:
                count += freq[current_xor ^ k]
    
            # Update the frequency of the current XOR in the map
            freq[current_xor] = freq.get(current_xor, 0) + 1
    
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends