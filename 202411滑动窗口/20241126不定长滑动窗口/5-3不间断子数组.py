from collections import Counter

## 不间断子数组
class Solution1:
	def continuousSubarrays(self,nums):
		ans=left=0
		dic_win=[]
		for right,c in enumerate(nums):
			dic_win.append(c)
			while max(dic_win)-min(dic_win)>2:
				dic_win=dic_win[1:]  # 复杂度O(n),所以会超出时间限制
				left+=1
			ans+=right-left+1
		return ans

class Solution2:
	def continuousSubarrays(self,nums):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(nums):
			dic_win[c]+=1
			while max(dic_win.keys())-min(dic_win.keys())>2:
				if dic_win[nums[left]]==1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]]-=1
				left+=1
			ans+=right-left+1
		return ans

if __name__ == '__main__':
	nums=[5,4,2,4]
	print(Solution2().continuousSubarrays(nums))