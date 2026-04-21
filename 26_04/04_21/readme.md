对于283，处理思路是用滑动窗口
一开始我设了双指针，left，right，但是更新的时候出问题了，直接在每次碰到相同元素的时候直接更新left, right但是没考虑中间可能有以别的元素为起点的子字符串长度更大
所以采用哈希表，left的更新值是hashmap[s[right]] + 1
还有每次的hashmap[s[right]] >= left判断也不可以少，这样检验重复元素是不是在我的串口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

