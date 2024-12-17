# 找出最长等值子数组
## 方法一：自写版
from collections import defaultdict


class Solution1:
	def longestEqualSubarray(self,nums,k):
		ans=left=0
		cnt=0
		all_dic=Counter(nums)
		win_lis=[]
		tmp=0
		for x in all_dic:
			if all_dic[x]>tmp:
				char=x
				tmp=all_dic[x]
		for right,c in enumerate(nums):
			while c!=char:
				left+=1
## 方法二：灵神滑动窗口思路
class Solution2:
	def longestEqualSubarray(self,nums,k):
		group_dic={}
		for i,c in enumerate(nums):
			if c in group_dic:
				group_dic[c].append(i-len(group_dic[c]))
			else:
				group_dic[c]=[i]
		ans=0
		for c in group_dic:
			if len(group_dic[c])<=ans:
				continue
			left=0
			c_lis=group_dic[c]
			for right,x in enumerate(c_lis):
				while x-c_lis[left]>k:
					left += 1
				ans=max(ans,right-left+1)
		return ans
## 方法三：灵神滑动窗口版
class Solution3:
    def longestEqualSubarray(self, nums, k):
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
	nums=[1,2,1]
	k=0
	s=Solution3()
	print(s.longestEqualSubarray(nums,k))