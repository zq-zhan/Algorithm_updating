from collections import Counter, defaultdict

class Solution:
	def specialTriplets(self, nums):
		MOD = 10 ** 9 + 7
		sub_dic = Counter(nums)
		pre_dic = defaultdict(int)
		ans = 0
		for i, x in enumerate(nums): # 枚举中间
			sub_dic[x] -= 1
			ans = (pre_dic[x * 2] * sub_dic[x * 2] + ans) % MOD
			pre_dic[x] += 1
		return ans
	
if __name__ == '__main__':
	nums = [8,4,2,8,4]
	print(Solution().specialTriplets(nums))