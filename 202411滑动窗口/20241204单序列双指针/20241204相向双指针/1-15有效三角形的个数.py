# 15.有效三角形的个数
class Solution1:  # 超出时间限制
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for a in range(0,n-2):
			for b in range(a+1,n-1):
				c=n-1
				while c>b:
					if nums[a]+nums[b]>nums[c]:
						cnt+=c-b
						break
					else:
						c-=1
		return cnt
## 滑动窗口逻辑
class Solution2:
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for a in range(0,n-2):
			b=a+1
			c=a+2
			while c<n:
				if nums[a]+nums[b]>nums[c]:
					cnt+=c-b
					c+=1
				elif b==c-1:
					c+=1
				else:
					b+=1
		return cnt
	
## 滑动窗口逻辑
class Solution3:
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for a in range(0,n-2):
			b=a+1
			c=a+2
			while c<n:
				if nums[a]+nums[b]>nums[c]:
					cnt+=c-b
					c+=1
				elif b<c-1:
					b+=1
				else:
					c+=1
		return cnt
	

# 灵神思路一：固定较大的指针
class Solution4:
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for c in range(2,n):
			a=0
			b=c-1
			while a<b:
				if nums[a]+nums[b]>nums[c]:
					cnt+=b-a  # 向右移动a都成立
					b-=1
				else:
					a+=1
		return cnt

class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for k in range(2, len(nums)):
            c = nums[k]
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] > c 同时意味着：
                    # nums[i+1]+nums[j] > c
                    # nums[i+2]+nums[j] > c
                    # ...
                    # nums[j-1]+nums[j] > c
                    # 从 i 到 j-1 一共 j-i 个
                    ans += j - i
                    j -= 1
                else:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] <= c 同时意味着
                    # nums[i]+nums[j-1] <= c
                    # ...
                    # nums[i]+nums[i+1] <= c
                    # 所以在后续的内层循环中，nums[i] 不可能作为三角形的边长，没有用了
                    i += 1
        return ans


if __name__=='__main__':
	nums=[24,3,82,22,35,84,19]
	cls=Solution2()
	print(cls.triangleNumber(nums))