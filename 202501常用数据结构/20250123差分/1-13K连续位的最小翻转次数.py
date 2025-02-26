# 13.K连续位的最小翻转次数
## 方法一：差分
class Solution1:
	def minKBitFlips(self, nums, k):
		n = len(nums)

		d = [0] * (n + 1)
		s = ans = 0
		for i in range(n):
			s += d[i]
			if (nums[i] + s) % 2 == 0:  # 判断经过前面的总翻转之后，当前是0
				if i + k > n:  # 剩余长度不够完成翻转
					return -1
				ans += 1
				s += 1
				d[i + k] -= 1  # 下台阶的位置
		return ans
	
if __name__ == '__main__':
	nums = [0,0,0,1,0,1,1,0]
	k = 3
	print(Solution1().minKBitFlips(nums, k)) 