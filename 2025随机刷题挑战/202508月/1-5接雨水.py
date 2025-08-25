## 灵神题解——前后缀分解
class Solution:
	def trap(self, height):
		n = len(height)
		pre_max = [0] * n  # pre_max[i]表示从height[0]到height[i]的最大值
		pre_max[0] = height[0]
		for i in range(1, n):
			pre_max[i] = max(pre_max[i - 1], height[i])

		suf_max = [0] * n  # 后缀最大值
		suf_max[-1] = height[-1]
		for i in range(n - 2, -1, -1):
			suf_max[i] = max(suf_max[i + 1], height[i])

		ans = 0
		for h, pre, suf in zip(height, pre_max, suf_max):
			ans += min(pre, suf) - h
		return ans
		

if __name__ == '__main__':
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	print(Solution().trap(height))