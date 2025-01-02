# 11.数组中最长的山脉
class Solution1:
	def longestMountain(self,arr):
		ans = 0
		i = 0
		n = len(arr)
		while i < n:
			start = i
			i += 1
			cnt_left = 0
			cnt_right = 0
			# cnt
			while i < n and arr[i] > arr[i - 1] and cnt_right == 0:
				i += 1
				cnt_left += 1
			while i < n and arr[i] < arr[i - 1] and cnt_left > 0:
				i += 1
				cnt_right += 1
			if cnt_left == cnt_right > 1:
				ans = max(ans,i - start)
			i = start + 1
		return ans

# 11.数组中最长的山脉
class Solution2:
	def longestMountain(self,nums):
		ans = 0
		i = 1
		n = len(nums)
		while i < n - 1:
			if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
				left = right = i
				while left > 0 and nums[left] > nums[left - 1]:
					left -= 1
				while right < n -1 and nums[right] > nums[right + 1]:
					right += 1
				# if i - left == right - i:
				ans = max(ans, right - left + 1)
			i += 1
		return ans
	
if __name__ == '__main__':
	arr = [0,1,2,3,4,5,4,3,2,1,0]
	s = Solution2()
	print(s.longestMountain(arr))