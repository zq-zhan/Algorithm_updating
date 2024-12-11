# 14.四数之和
class Solution1:
	def fourSum(self,nums,target):
		nums.sort()
		ans=[]
		n=len(nums)
		for a in range(n-3):
			if a and nums[a]==nums[a-1]:
				continue
			d=n-1
			while a<d:
				x1=nums[a]
				x4=nums[d]
				b=a+1
				c=d-1
				while b<c:
					s=x1+nums[b]+nums[c]+x4
					if s==target:
						ans.append([x1,nums[b],nums[c],x4])
						b+=1
						while nums[b]==nums[b-1] and b<c:
							b+=1 
						c-=1
						while nums[c]==nums[c+1] and c>b:
							c-=1
					elif s<target:
						b+=1
						# if nums[b]==nums[b-1] and b<c:
						# 	b+=1
					else:
						c-=1
						# if nums[c]==nums[c+1] and c>b:
						# 	c-=1
				d-=1
				while nums[d]==nums[d+1] and d>a:
					d-=1
		return ans

## 灵神思路
class Solution2:  # 枚举前两个数
	def fourSum(self,nums,target):
		nums.sort()
		ans=[]
		n=len(nums)
		for a in range(n-3):
			x1=nums[a]
			if a and nums[a-1]==nums[a]:
				continue
			if nums[a]+nums[-3]+nums[-2]+nums[-1]<target:
				continue
			if nums[a]+nums[a+1]+nums[a+2]+nums[a+3]>target:
				break
			for b in range(a+1,n-2):
				x2=nums[b]
				if b>a+1 and nums[b]==nums[b-1]:  # 注意这里b>a+1条件易错，因为要排除第一个b和a相同的情况，这个不需要跳过
					continue
				if x1+nums[b]+nums[-2]+nums[-1]<target:
					continue
				if x1+nums[b]+nums[b+1]+nums[b+2]>target:
					break
				c=b+1
				d=n-1
				while c<d:
					x3=nums[c]
					x4=nums[d]
					s=x1+x2+x3+x4
					if s==target:
						ans.append([x1,x2,x3,x4])
						c+=1
						while c<d and nums[c]==nums[c-1]:
							c+=1
						d-=1
						while d>c and nums[d]==nums[d+1]:
							d-=1
					elif s>target:
						d-=1
					else:
						c+=1
		return ans

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n - 3):  # 枚举第一个数
            x = nums[a]
            if a and x == nums[a - 1]:  # 跳过重复数字
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:  # 优化一
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for b in range(a + 1, n - 2):  # 枚举第二个数
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]:  # 跳过重复数字
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:  # 优化一
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                # 双指针枚举第三个数和第四个数
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]  # 四数之和
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:  # s == target
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                            d -= 1
        return ans


if __name__=="__main__":
	nums=[2,2,2,2,2]
	target=8
	s=Solution2()
	print(s.fourSum(nums,target))