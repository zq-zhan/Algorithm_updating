# 20250112——按位与结果大于零的最长组合
class Solution1:
	def largestCombination(self, candidates):
		ans = 1
		left = 0
		n = len(candidates)
		
		while left < n:
			right = left + 1
			temp_result = candidates[left]
			temp_ans = 1
			while right < n:
				if temp_result & candidates[right] > 0:
					temp_ans += 1
				right += 1
			ans = max(ans, temp_ans)
			left += 1
		return ans
## 灵神思路：枚举比特位
class Solution2:
	def largestCombination(self, candidates):
		m = max(candidates).bit_length()
		return max(sum(x >> i & 1 for x in candidates) for i in range(m))
	
if __name__ == '__main__':
	candidates = [16,17,71,62,12,24,14]
	cls = Solution2()
	print(cls.largestCombination(candidates))