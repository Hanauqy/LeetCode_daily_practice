from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #left = 0
        #ans = -10000
        #while left + k <= len(nums):
            # sum = 0
            # for j in range(left, left + k):
            #     sum += nums[j]
            # ans = max(ans, sum/k)
            # left +=1
        
        #return ans

        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        
        return maxTotal / k


# ===================== 主函数 + 测试案例 =====================
if __name__ == "__main__":
    sol = Solution()

    # 测试用例1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    print("测试用例1：", sol.findMaxAverage(nums1, k1))  # 预期 12.75

    # 测试用例2
    nums2 = [5]
    k2 = 1
    print("测试用例2：", sol.findMaxAverage(nums2, k2))  # 预期 5.0

    # 测试用例3
    nums3 = [-1, -2, -3, -4]
    k3 = 2
    print("测试用例3：", sol.findMaxAverage(nums3, k3))  # 预期 -1.5