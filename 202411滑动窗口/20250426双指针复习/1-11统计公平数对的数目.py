class Solution1:
	def countFairPairs(self, nums, lower, upper):
		ans = 0
		for i, c in enumerate(nums):
			for j in range(i + 1, len(nums)):
				if lower <= c + nums[j] <= upper:
					ans += 1
		return ans
## 优化
class Solution2:
	def countFairPairs(self, nums, lower, upper):
		new_arr = []
		for i, c in enumerate(nums):
			new_arr.append([c, i])
		new_arr = sorted(new_arr, key = lambda x:x[0])

		ans = 0
		left, right = 0, len(nums) - 1
		while left < right:
			temp_s = new_arr[left][0] + new_arr[right][0]
			if lower <= temp_s <= upper:
				for i in range(left + 1, right):
					if new_arr[i][1] > new_arr[left][1]:
						ans += 1
			elif temp_s < lower:
				left += 1
			else:
				right -= 1
		return ans
	

class Solution:
    def countFairPairs(self, nums, lower, upper) -> int:
        nums.sort()
        res=0
        n=len(nums)
        l,r=n-1,n-1
        for i in range(n):
            while r>0 and nums[i]+nums[r]>upper:#找到第一个满足的r
                r-=1
            while l>0 and nums[i]+nums[l]>=lower:#找到第一个不满足的l
                l-=1
            res+=min(i,r)-min(i,l)
        return res
	
if __name__ == '__main__':
	nums = [0,1,7,4,4,5]
	lower = 3
	upper = 6
	print(Solution().countFairPairs(nums, lower, upper))