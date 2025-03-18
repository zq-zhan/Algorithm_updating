from collections import defaultdict, deque
from sortedcontainers import SortedList

class Solution:
	def longestSubarray(self, nums, limit):
		temp_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win[c] += 1
			if max(temp_win) - min(temp_win) <= limit:
				ans = max(ans, right - left + 1)
				continue
			if temp_win[nums[left]] == 1:
				del temp_win[nums[left]]
			else:
				temp_win[nums[left]] -= 1
			left += 1
		return ans
##
class Solution1:  # 因为循环内取max所以复杂度为O(n^2)
	def longestSubarray(self, nums, limit):
		temp_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max(temp_win) - min(temp_win) > limit:
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
### 优化1：有序列表
class Solution2:
	def longestSubarray(self, nums, limit):
		temp_win = SortedList()
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win.add(c)
			while temp_win[-1] - temp_win[0] > limit:
				temp_win.remove(nums[left])
				left += 1
			ans = max(ans, right - left + 1)
		return ans
### 优化2：维护两个队列
class Solution3:
	def longestSubarray(self, nums, limit):
		# temp_win = SortedList()
		ans = left = 0
		min_deque = deque()
		max_deque = deque()
		for right, c in enumerate(nums):
			while max_deque and c > max_deque[-1]:
				max_deque.pop()
			max_deque.append(c)
			while min_deque and c < min_deque[-1]:
				min_deque.pop()  # 反向比较，如果当前值小于队列尾部元素，则弹出队列尾部元素
			min_deque.append(c)  # 按窗口顺序为两个队列添加元素，使得队列头部为当前窗口的最大值和最小值

			while max_deque[0] - min_deque[0] > limit:
				nums_left = nums[left]
				if nums_left == max_deque[0]:
					max_deque.popleft()
				if nums_left == min_deque[0]:
					min_deque.popleft()
				left += 1
			ans = max(ans, right - left + 1)
		return ans

	
if __name__ == '__main__':
	nums = [10,1,2,4,7,2]
	limit = 5
	print(Solution3().longestSubarray(nums, limit))