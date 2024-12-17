# 5.按奇偶排序数组2
class Solution1:
	def sortArrayByParityII(self,nums):
		slow=0
		for fast in range(len(nums)):
			while (nums[fast]%2==0 and slow%2==0) or (nums[fast]%2==1 and slow%2==1):
				temp=nums[slow]
				nums[slow]=nums[fast]
				nums[fast]=temp
				slow+=1
		return nums

class Solution2:
	def sortArrayByParityII(self,nums):
		slow=0
		for fast in range(1,len(nums),2):  # 找到奇数索引下为偶数的值传递给偶数索引
			while nums[fast]%2==0:
				temp=nums[fast]
				nums[fast]=nums[slow]
				nums[slow]=temp
				slow+=2
		return nums

if __name__ == '__main__':
	nums=[4,1,3,2]
	s=Solution1()
	print(s.sortArrayByParityII(nums))