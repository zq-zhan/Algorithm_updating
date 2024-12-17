# 13.最接近的三数之和
from math import inf


class Solution1:
	def threeSumClosest(self,nums,target):
		nums.sort()
		temp_sum=inf
		n=len(nums)
		for i in range(n-2):
			x=nums[i]
			j=i+1
			k=n-1
			while j<k:
				win_sum=x+nums[j]+nums[k]
				if abs(win_sum-target)<abs(temp_sum-target):
					temp_sum=win_sum
					if win_sum-target==0:
						return temp_sum
				if win_sum<target:
					j+=1
				else:
					k-=1
		return temp_sum
	
## 灵神思路：添加三个优化点## 灵神思路：添加三个优化点
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  # 优化三

            # 优化一
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:  # s 与 target 更近
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:  # s < target
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans


	
if __name__=='__main__':
	nums=[-1,2,1,-4]
	target=1
	s=Solution1()
	print(s.threeSumClosest(nums,target))