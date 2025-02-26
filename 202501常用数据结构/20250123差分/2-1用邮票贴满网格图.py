###################### 二维差分 ####################
# 1.用邮票贴满网格图
## 灵神二维差分思路
class Solution1:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m, n = len(grid), len(grid[0])

        # 1.计算grid的二维前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2.计算二维差分，实现对stampWeight* stampHeight的网格填充，后续对这个填充后的网格还原后便是邮票覆盖后的网格
        ## 为方便计算，在d数组的最上面和最左边各家了一行
        d = [[0] * (n + 2) for _ in range(m + 2)]
        # # 写法二
        # for i2 in range(1, m - stampHeight + 2):
        #     for j2 in range(1, n - stampWidth + 2):
        #         if s[i2][j2] - s[i2][j2 - 1] - s[i2 - 1][j2] + s[i2 - 1][j2 -1] == 0:  # 在未被占据时才可以使用邮票覆盖
        #             d[i2][j2] = 1
        #             d[i2][j2 + stampWidth] = -1
        #             d[i2 + stampHeight][j2] = -1
        #             d[i2 + stampHeight][j2 + stampWidth] = 1
        for i2 in range(stampHeight, m + 1):
            for j2 in range(stampWidth, n + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if s[i2][j2] - s[i2][j1 - 1] - s[i1 - 1][j2] + s[i1 - 1][j1 - 1] == 0:  # 用前缀和的差计算得到当前格子的邮票覆盖情况
                    d[i1][j1] += 1
                    d[i1][j2 + 1] -= 1
                    d[i2 + 1][j1] -= 1
                    d[i2 + 1][j2 + 1] += 1

        # 3. 还原二维差分矩阵对应的计数矩阵（原地计算）
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                d[i + 1][j + 1] += d[i + 1][j] + d[i][j + 1] - d[i][j]
                if v == 0 and d[i + 1][j + 1] == 0:
                    return False
        return True
    
if __name__ == '__main__':
    cls = Solution1()
    grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    stampHeight, stampWidth = 2,2
    print(cls.possibleToStamp(grid, stampHeight, stampWidth)) # True