from collections import Counter

## 统计完全子数组的数目
class Solution1:
	def countCompleteSubarrays(self,nums):
		ans=left=0
		dic_all=Counter(nums)
		dic_win=Counter()
		n=len(dic_all)
		for right,c in enumerate(nums):
			dic_win[c]+=1
			while len(dic_win)==n:
				if dic_win[nums[left]]==1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]]-=1
				left+=1
			ans+=left
		return ans
	
class Solution1:
	def countCompleteSubarrays(self, nums):
		target_num = len(set(nums))
		set_win = []
		ans = left = 0
		for right, c in enumerate(nums):
			set_win.append(c)
			while len(set(set_win)) == target_num:
				set_win = set_win[1:]
				left += 1
			ans += left
		return ans
	
if __name__=='__main__':
	nums=[1,3,1,2,2]
	s=Solution1()
	print(s.countCompleteSubarrays(nums))