class Solution1:
	def findDuplicate(self, nums):
		for i in range(1, len(nums) + 1):
			if nums.count(i) > 1:
				return i
			
class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        while True:
            # fast 前进两次，slow 前进一次
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break

        # ptr == slow 时说明检测到重复元素，两个重复元素同时指向环的入口。
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr


## 二分解法
class Solution2:
	def findDuplicate(self, nums):
		min_val = 1
		max_val = max(nums)
		while min_val < max_val:
			mid = (min_val + max_val) // 2
			cnt = sum(min_val <= num <= mid for num in nums)
			if cnt > mid - min_val + 1:
				max_val = mid
			else:
				min_val = mid + 1
		return min_val

## 二分解法--开区间写法
class Solution3:
	def findDuplicate(self, nums):
		min_val = 0
		max_val = max(nums) + 1
		while min_val + 1 < max_val:
			mid = (min_val + max_val) // 2
			cnt = sum(min_val <= num <= mid for num in nums)
			if cnt > mid - min_val + 1:
				max_val = mid
			else:
				min_val = mid
		return min_val


if __name__ == '__main__':
	nums = [3,1,3,4,2]
	print(Solution3().findDuplicate(nums))