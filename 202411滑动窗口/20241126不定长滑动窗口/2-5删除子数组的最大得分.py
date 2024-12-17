# 删除子数组的最大得分
## 方法一：自写版
class Solution1():
	def maximumUniqueSubarray(self,nums):
		ans=left=0
		total=0
		window=set()
		for right,c in enumerate(nums):
			# window.add(c)
			while c in window:
				window.remove(nums[left])
				total-=nums[left]
				left += 1
			window.add(c)
			total+=c
			ans = max(ans,total)
		return ans

if __name__ == '__main__':
	nums = [5,2,1,2,5,2,1,2,5]
	s = Solution1()
	print(s.maximumUniqueSubarray(nums))