# 6.132模式
from math import inf

class Solution1:
	def find132pattern(self, nums):
		n = len(nums)
		pre_min = [nums[0]] * n
		for l in range(1, n):
			pre_min[l] = min(pre_min[l - 1], nums[l])
		for j in range(n - 2, 0, -1):
			k = j + 1
			while k < n:
				if pre_min[j - 1] < nums[k] < nums[j]:
					return True
				k += 1
		return False
	
## 枚举k
class Solution2:
	def find132pattern(self, nums):
		n = len(nums)
		pre_min = [nums[0]] * n
		for l in range(1, n):
			pre_min[l] = min(pre_min[l - 1], nums[l])
		mid_max = [nums[0]] * n
		for h in range(1, n):
			mid_max[h] = max(mid_max[h - 1], nums[h])
		for k in range(2, n):
			if pre_min[k - 2] < nums[k] < mid_max[k - 1]:
				return True
		return False
	
## 灵神题解
class Solution3:
	def find132pattern(self, nums):
		n = len(nums)
		st = []
		k = -inf
		for i in range(n - 1, -1, -1):
			if nums[i] < k:
				return True
			while st and nums[i] > nums[st[-1]]:
				k = nums[st.pop()]
			st.append(i)
		return False

## 栈解法
class Solution4:
	def find132pattern(self, nums):
		le = len(nums)
		if le < 2:
			return False

		mi = [nums[0]]  # 前缀和最小值
		for i in range(1, le):
			mi.append(min(nums[i], mi[-1]))

		stack = []
		for i in range(le - 1, -1, -1):
			print(stack)
			if nums[i] > mi[i]:
				while stack and mi[i] >= stack[-1]:
					stack.pop()  # 移除栈顶元素

				if stack and stack[-1] < nums[i]:
					return True
				stack.append(nums[i])
		return False
	
class Solution:
    def find132pattern(self, nums):

        n = len(nums)
        st = []
        k = -inf 
        for i in range(n - 1, -1, -1):
            if nums[i] < k: # 这里的判断 i k就是第三个数
                return True
            while st and nums[i] > st[-1]:
                k = st.pop()    # 那就是小于nums[j]的最大的数字
            st.append(nums[i])
        return False

if __name__ == '__main__':
	nums = [1,2,3,4,-4,-3,-5,-1]
	cls = Solution()
	print(cls.find132pattern(nums))