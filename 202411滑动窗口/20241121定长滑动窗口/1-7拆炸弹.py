# 4.拆炸弹
class Solution1:
	def decrypt(self, code, k):
		n = len(code)
		if k == 0:
			return [0] * n
		ans = []
		code = code + code + code
		for i in range(n, 2 * n):
			if k > 0:
				ans.append(sum(code[i + 1:i + k + 1]))
			else:
				ans.append(sum(code[i + k:i]))
		return ans

## 分类讨论
class Solution2:
	def decrypt(self, code, k):
		res_lis = []
		temp_ans = 0
		n = len(code)
		if k > 0:
			new_arr = code[1:] + code
		elif k < 0:
			new_arr = code[k:] + code
		else:
			return [0] * n

		# cnt = 0
		abs_k = abs(k)
		for left, x in enumerate(new_arr):
			temp_ans += x
			# cnt += 1
			if left >= abs_k - 1:
				res_lis.append(temp_ans)
				temp_ans -= new_arr[left - abs_k + 1]
			if len(res_lis) == n:
				break
		return res_lis

if __name__== '__main__':
	code = [2,4,9,3]
	k = -2
	print(Solution2().decrypt(code, k))