# 2.删除有序数组中的重复项
class Solution1:
	def removeDuplicates(self,nums):
		k=1
		for i in range(1,len(nums)):
			if nums[i]!=nums[i-1]:
				nums[k]=nums[i]
				k+=1
		return k
	
class Solution2:
    def removeDuplicates(self, nums):
#用指针进行数组的遍历
        n = len(nums)
#i是快指针，进行数组的遍历，j是慢指针，用来指向答案的位置
        j = 0
        for i in range(n):
            if i ==0 or nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j    
    

class Solution3:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # nums[i] 不是重复项
                nums[k] = nums[i]  # 保留 nums[i]
                k += 1
        return k

if __name__ == '__main__':
	nums=[0,0,1,1,1,2,2,3,3,4]
	s=Solution2()
	print(s.removeDuplicates(nums))