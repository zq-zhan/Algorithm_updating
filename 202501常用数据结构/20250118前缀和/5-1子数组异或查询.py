# 前缀异或和
# 1.子数组异或查询
class Solution1:
	def xorQueries(self, arr, queries):
		ret = []
		for i in range(1, len(arr)):
			arr[i] ^= arr[i - 1]
		for left, right in queries:
			if left == 0:
				ret.append(arr[right])
			else:
				ret.append(arr[right] ^ arr[left - 1])
		return ret
	
class Solution2:
	def xorQueries(self, arr, queries):
		# ret = []
		pre_sum = [0] * (len(arr) + 1)
		for i in range(len(arr)):
			pre_sum[i + 1] = pre_sum[i] ^ arr[i]
		ans = []
		for left, right in queries:
			ans.append(pre_sum[right + 1] ^ pre_sum[left])
		return ans
	
if __name__ == '__main__':
	arr = [1, 3, 4, 8]
	queries = [[0,1],[1,2],[0,3],[3,3]]
	cls = Solution2()
	print(cls.xorQueries(arr, queries))