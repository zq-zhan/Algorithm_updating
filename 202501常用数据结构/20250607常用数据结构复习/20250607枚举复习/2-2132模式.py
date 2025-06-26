from math import inf

class Solution:
	def find132pattern(self, nums):
		n = len(nums)
		suf_mn = [inf] * (n + 1)
		suf_mx = [-inf] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_mx[i] = max(suf_mx[i + 1], nums[i])
			suf_mn[i] = min(suf_mn[i + 1], nums[i])

		pre_mn = nums[0]
		for j, x in enumerate(nums):
			# if suf_mn[j + 1] >= x or suf_mx[j + 1] <= pre_mn:
			# 	pre_mn = min(pre_mn, x)
			# else:
			# 	return True

			if pre_mn <= suf_mn[j + 1] <= x or pre_mn <= suf_mx[j + 1] <= x:
				return True
			pre_mn = min(pre_mn, x)
		return False
	

class Solution:
    def find132pattern(self, nums):

        n = len(nums)
        st = []
        k = -inf 
        for i in range(n - 1, -1, -1):
            if nums[i] < k: # 这里的判断 i k就是第三个数
                return True
            while st and nums[i] > nums[st[-1]]:
                k = nums[st.pop()]    # 那就是小于nums[j]的最大的数字
            st.append(i)
        return False

## 正确思路：如何在j + 1至 n - 1找到比nums[j]小但比nums[i]大的元素——栈
class Solution:
	def find132pattern(self, nums):
		n = len(nums)
		pre_mn = [nums[0]]
		for i in range(1, n):
			pre_mn.append(min(pre_mn[i - 1], nums[i]))

		st = []
		for j in range(n - 1, 0, -1):
			if nums[j] > pre_mn[j - 1]:
				while st and pre_mn[j - 1] >= st[-1]:
					st.pop()
				if st and st[-1] < nums[j]:
					return True
				st.append(nums[j])
		return False

if __name__ == '__main__':
	nums = [3,1,2]
	print(Solution().find132pattern(nums))