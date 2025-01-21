# 3.大小为k且平均值大于等于阈值的子数组数目
class Solution1:
	def numOfSubarrays(self, arr, k, threshold):
		ans = 0
		temp_sum = 0
		for i, c in enumerate(arr):
			temp_sum += c
			if i < k - 1:
				continue
			# while temp_sum / k >= threshold:
			ans += 1 if temp_sum / k >= threshold else 0
			temp_sum -= arr[i - k + 1]
		return ans
	
if __name__ == '__main__':
	arr = [2, 2, 2, 2, 5, 5, 5, 8]
	k = 3
	threshold = 4
	cls = Solution1()
	print(cls.numOfSubarrays(arr, k, threshold))