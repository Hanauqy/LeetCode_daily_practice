from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_size = 0
        hashmap = {}
        
        for right in range(len(s)):
            # 当前字符 已经在窗口里
            if s[right] in hashmap and hashmap[s[right]] >= left:
                left = hashmap[s[right]] + 1  # 移动左边界
            
            hashmap[s[right]] = right
            
            max_size = max(max_size, right - left + 1)
        
        return max_size
        return max_size
        


if __name__ == "__main__":
    sol = Solution()

    s1 = "abcabcbb"
    print(f"输入: {s1}, 输出: {sol.lengthOfLongestSubstring(s1)}  预期: 3")

    s2 = "bbbbb"
    print(f"输入: {s2}, 输出: {sol.lengthOfLongestSubstring(s2)}  预期: 1")

    s3 = "pwwkew"
    print(f"输入: {s3}, 输出: {sol.lengthOfLongestSubstring(s3)}  预期: 3")

    s4 = ""
    print(f"输入: {s4}, 输出: {sol.lengthOfLongestSubstring(s4)}  预期: 0")

    s5 = "a"
    print(f"输入: {s5}, 输出: {sol.lengthOfLongestSubstring(s5)}  预期: 1")