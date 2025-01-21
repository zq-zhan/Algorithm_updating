# 3.和有限的最长子序列
class Solution1:  # 这个解法是子数组！！！
	def answerQueries(self, nums, queries):
		# nums.sort()
		suf_sum = [0]
		for x in nums:
			suf_sum.append(suf_sum[-1] + x)
		# suf_sum.append(suf_sum[-1] + nums[-1])
		n = len(suf_sum)

		ans = []
		for target in queries:
			temp = 0
			left = 0
			for right in range(1, n):
				if suf_sum[right] - suf_sum[left] <= target:
					temp = max(temp, right - left)
					# right += 1
					continue
				left += 1
			ans.append(temp)
		return ans
	
if __name__ == '__main__':
    nums = [4,5,2,1]
    queries = [3,10,21]
    cls = Solution1()
    print(cls.answerQueries(nums, queries))