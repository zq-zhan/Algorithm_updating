# 5.美化数组的最少删除数
class Solution1:
	def minDeletion(self, nums):
		n = len(nums)
		ans = 0
		st = []
		for c in nums:
			if st and (len(st) - 1) % 2 == 0 and st[-1] == c:
				# st.pop()
				ans += 1
			else:
				st.append(c)
		return ans + len(st) % 2
	
# 优化掉栈
class Solution2:
	def minDeletion(self, nums):
		ans, length = 0, -1
		before_chr = 'a'
		for c in nums:
			if length % 2 == 0 and before_chr == c:
				ans += 1
				# length -= 1
			else:
				before_chr = c
				length += 1
		return ans + (length + 1) % 2
	
if __name__ == '__main__':
	nums = [1,1,2,2,3,3]
	print(Solution2().minDeletion(nums)) # Output: 1