# 8.两数之和-输入有序数组
class Solution1:
	def twoSum(self,numbers,target):
		n=len(numbers)
		left,right=0,n-1
		while left<right:
			temp_sum=numbers[left]+numbers[right]
			if temp_sum>target:
				right-=1
			elif temp_sum<target:
				left+=1
			else:
				return [left,right]
		return [-1,-1]
		
if __name__=="__main__":
	numbers=[2,7,11,15]
	target=9
	s=Solution1()
	print(s.twoSum(numbers,target))