class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        visited = set()
        curr_window_size = 0 
        longest = 0 

        while r < len(s): 
            if s[r] not in visited: 
                curr_window_size += 1 
                visited.add(s[r])
                r += 1 
            else: 
                while s[r] in visited: 
                    visited.remove(s[l])
                    l += 1 
                    curr_window_size -= 1 
            longest = max(longest, curr_window_size)

        return longest 
            


        