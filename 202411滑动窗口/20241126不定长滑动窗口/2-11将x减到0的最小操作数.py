# 将x减到0的最小操作数
## 方法一：逆向思维
class Solution1():
	def minOperations(self,nums,k):
		ans=-1
		left=0
		total_win=0
		total=sum(nums)
		target_num=total-k
		if target_num<0:
			return -1
		for right,c in enumerate(nums):
			total_win+=c
			while total_win>target_num:
				total_win -= nums[left]
				left += 1
			if total_win==target_num:
				# cnt+=1
				ans=max(ans,right-left+1)
		if ans!=-1:
			return len(nums)-ans
		else:
			return -1

## 方法二：灵神，双指针正向计算		
class Solution2:
    def minOperations(self, nums,x):
        s, n = 0, len(nums)
        right = n
        while right and s + nums[right - 1] <= x:  # 计算最长后缀
            right -= 1
            s += nums[right]
        if right == 0 and s < x: return -1  # 全部移除也无法满足要求
        ans = n - right if s == x else 'inf'
        for left, num in enumerate(nums):
            s += num
            while right < n and s > x:  # 缩小后缀长度
                s -= nums[right]
                right += 1
            if s > x: break  # 缩小失败，说明前缀过长
            if s == x: ans = min(ans, left + 1 + n - right)  # 前缀+后缀长度
        return ans if ans <= n else -1


if __name__=="__main__":
	nums=[3,2,20,1,1,3]
	k=10
	s=Solution2()
	print(s.minOperations(nums,k))