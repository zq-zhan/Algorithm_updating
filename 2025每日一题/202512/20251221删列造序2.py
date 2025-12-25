class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        ans = 0
        # is_sorted[i] 为 True 表示 strs[i] < strs[i+1] 已经确定了
        is_sorted = [False] * (n - 1)
        
        for j in range(m):
            can_keep = True
            for i in range(n - 1):
                # 只有在还没分出胜负的情况下，才需要比较当前列
                if not is_sorted[i]:
                    if strs[i][j] > strs[i + 1][j]:
                        can_keep = False
                        break
            
            if can_keep:
                # 如果这一列被保留，更新已经分出胜负的行
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        is_sorted[i] = True
                # 如果所有行都分出胜负了，直接返回
                if all(is_sorted):
                    return ans
            else:
                ans += 1
                
        return ans
			
if __name__ == '__main__':
	strs = ["xga","xfb","yfa"]
	print(Solution().minDeletionSize(strs))