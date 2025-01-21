# 5.任意子数组和的绝对值的最大值
class Solution1:
	def maxAbsoluteSum(self, nums):
		# 转换为在前缀和数组中找和最大的子数组
		pre_sum = [0]
		for p1 in range(len(nums)):
			pre_sum.append(pre_sum[-1] + nums[p1])
		# ans = 0
		# for i in range(len(pre_sum)):
		# 	for j in range(len(pre_sum)):
		# 		ans = max(abs(pre_sum[j] - pre_sum[i]), ans)
		return max(pre_sum) - min(pre_sum)
## 滑动窗口思路
class Solution2:
	def maxAbsoluteSum(self, nums):
		def max_sum(max_num, new_arr):
			ans = max_num
			left = 0
			dic_sum = 0
			for right, c in enumerate(new_arr):
				dic_sum += c
				if dic_sum >= ans:
					# dic_sum += c
					ans = max(dic_sum,ans)
					continue
				dic_sum -= new_arr[left]
				ans = max(dic_sum,ans)
				left = right + 1
			return ans
		ans_re = max_sum(0, nums)
		nums = [-x for x in nums]
		ans_re = max(max_sum(0, nums), ans_re)
		return ans_re
	

if __name__ == '__main__':
	nums = [1,-3,2,3,-4]
	s = Solution2()
	print(s.maxAbsoluteSum(nums))