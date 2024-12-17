from collections import Counter

# 3.删除有序数组中的重复项2
class Solution1:
	def removeDuplicates(self,nums):
		win_dic=Counter()
		cnt=0
		for i in range(0,len(nums)):
			win_dic[nums[i]]+=1
			if win_dic[nums[i]]<=2:
				cnt+=1
				nums[cnt-1]=nums[i]
		return cnt
## 思路二：在有序条件下成立
class Solution2:
	def removeDuplicates(self,nums):
		k=2
		for i in range(2,len(nums)):
			if nums[i]!=nums[k-2]:
				nums[k]=nums[i]
				k+=1
		return k
	

if __name__=="__main__":
	nums=[1,1,1,2,2,3]
	s=Solution2()
	print(s.removeDuplicates(nums))