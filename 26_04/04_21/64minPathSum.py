from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # m = len(grid[0])

        # down = float('inf')
        # right = float('inf')

        # if n == 1 and m == 1:
        #     return grid[0][0]

        # if n > 1:
        #     sub_down = grid[1:]
        #     down = self.minPathSum(sub_down)
        
        # if m > 1:
        #     sub_right = [row[1:] for row in grid]
        #     right = self.minPathSum(sub_right)
        
        # return grid[0][0] + min(down, right)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i ==0 and j == 0:
                    continue
                elif j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
                else: grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        
        return grid[-1][-1]

# ===================== 主函数 + 测试用例 =====================
if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(f"输入: {grid1}")
    print(f"输出: {sol.minPathSum(grid1)}  预期: 7\n")

    # 测试用例 2
    grid2 = [[1,2,3],[4,5,6]]
    print(f"输入: {grid2}")
    print(f"输出: {sol.minPathSum(grid2)}  预期: 12\n")

    # 测试用例 3（只有1个数字）
    grid3 = [[5]]
    print(f"输入: {grid3}")
    print(f"输出: {sol.minPathSum(grid3)}  预期: 5\n")

    # 测试用例 4（只有一行）
    grid4 = [[1,2,3,4]]
    print(f"输入: {grid4}")
    print(f"输出: {sol.minPathSum(grid4)}  预期: 10")