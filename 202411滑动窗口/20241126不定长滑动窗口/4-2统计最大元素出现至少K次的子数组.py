# 越长越合法
## 统计最大元素出现至少K次的子数组
class Solution1:
	def countSubarrays(self,nums,k):
		ans=left=0
		max_data=max(nums)
		cnt=0
		for right,c in enumerate(nums):
			if c==max_data:
				cnt+=1
			while cnt>=k:
				cnt-=1 if nums[left]==max_data else 0
				left+=1
			ans+=left
		return ans
### 思路2
class Solution2:
	def countSubarrays(self,nums,k):
		ans=left=0
		n=len(nums)
		mx=max(nums)
		cnt=0
		for right,c in enumerate(nums):
			if c==mx:
				cnt+=1
			while cnt>=k:
				ans+=n-right
				if nums[left]==mx:
					cnt-=1
				left+=1
		return ans
	
# 2.统计最大元素出现至少K次的子数组
class Solution1:
	def countSubarrays(self, nums, k):
		mx = max(nums)
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while dic_win[mx] >= k:
				dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans

if __name__ == '__main__':
	nums=[1,3,2,3,3]
	k=2
	cls=Solution1()
	print(cls.countSubarrays(nums,k))