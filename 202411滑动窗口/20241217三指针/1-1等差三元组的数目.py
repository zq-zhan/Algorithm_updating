# 1.等差三元组的数目
class Solution1:
	def arithmeticTriplets(self,nums,diff):
		p1 = 0
		ans = 0
		n = len(nums)
		while p1 < n - 2:
			p2 = p1 + 1
			p3 = p2 + 1
			while p2 < n -1 and p3 < n:
				if nums[p3] - nums[p2] < diff:
					p3 += 1
				if nums[p2] - nums[p1] < diff:
					p2 += 1
					p3 += 1
				if nums[p2] - nums[p1] == nums[p3] - nums[p2] == diff:
					ans += 1
					p2 += 1
					p3 += 1
		return ans
# 灵神思路
class Solution2:
	def arithmeticTriplets(self,nums,diff):
		ans, i, j = 0, 0, 1
		for x in nums:  # 枚举第三个数
			while nums[j] + diff < x:
				j += 1
			if nums[j] + diff > x:
				continue
			while nums[i] + diff * 2 < x:
				i += 1
			if nums[i] + diff * 2 == x:
				ans += 1
		return ans

class Solution3:
	def arithmeticTriplets(self,nums,diff):
		ans, i, j, k = 0, 0, 1, 2
		n = len(nums)
		while k < n:  # 枚举第三个数
			while nums[j] + diff < nums[k]:
				j += 1
			if nums[j] + diff > nums[k]:
				k += 1
				continue
			while nums[i] + diff * 2 < nums[k]:
				i += 1
			if nums[i] + diff * 2 == nums[k]:
				ans += 1
			k += 1
		return ans
	
if __name__ == '__main__':
	nums = [0,1,4,6,7,10]
	diff = 3
	print(Solution2().arithmeticTriplets(nums,diff))