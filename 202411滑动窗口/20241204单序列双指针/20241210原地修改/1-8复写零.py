# 7.复写零
class Solution1:
	def duplicateZeros(self,nums):
		i=0
		while i < len(nums)-1:
			if nums[i]==0:
				for j in range(len(nums)-1,i+1,-1):
					nums[j]=nums[j-1]
				nums[i+1]=0
				i+=1
			i+=1
		return nums

## 思路二：O(n)
class Solution2:
	def duplicateZeros(self,arr):
		n=len(arr)
		zeros_num=sum(1 for x in arr if x==0)
		j=n+zeros_num-1

		for i in range(n-1,-1,-1):
			if j<n:
				arr[j]=arr[i]
			j-=1
			if arr[i]==0:
				if j<n:
					arr[j]=0
				j-=1
		return arr	

## 思路三：栈
class Solution3:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        idx, cnt = 0, 0
        while cnt < n:
            if arr[idx] == 0:
                cnt += 1
            idx += 1
            cnt += 1
        i, j = n - 1, idx - 1
        if arr[j] == 0 and cnt > n:
            arr[i] = 0
            i -= 1
            j -= 1
        while i > 0:
            arr[i] = arr[j]
            i -= 1
            if arr[j] == 0:
                arr[i] = 0
                i -= 1
            j -= 1
        return arr

if __name__ == '__main__':
	nums = [1,0,2,3,0,4,5,0]
	s=Solution3()
	print(s.duplicateZeros(nums))