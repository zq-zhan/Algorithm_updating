# 20.三数之和的多种可能
class Solution1:
	def threeSumMulti(self, arr, target):
		arr.sort()
		mod = 10 ** 9 + 7
		ans = 0

		def upper(i, target):
			temp_ans = 0
			left, right = i + 1, len(arr) - 1
			while left < right:
				if arr[i] + arr[left] + arr[right] <= target:
					temp_ans += right - left
					left += 1
				else:
					right -= 1
			return temp_ans

		for i in range(len(arr) - 2):
			ans += upper(i, target) - upper(i, target - 1)
		return ans % mod
	
if __name__ == '__main__':
	arr = [1,1,2,2,2,2]
	target = 5
	print(Solution1().threeSumMulti(arr, target))