from collections import defaultdict

class Solution1:
	def numOfSubarrays(self, arr):
		pre_sum = [0] * (len(arr) + 1)
		for i, c in enumerate(arr):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for pre_s in pre_sum:
			ans += cnt[1 - pre_s % 2]
			cnt[pre_s % 2] += 1
		return ans % (10 ** 9 + 7)

## 
# class Solution2:
# 	def numOfSubarrays(self, arr):
# 		pre_sum = [0] * (len(arr) + 1)
# 		for i, c in enumerate(arr):
# 			pre_sum[i + 1] = pre_sum[i] + c

# 		ans = 0
# 		# cnt = defaultdict(int)
# 		cnt = [0, 0]
# 		for pre_s in pre_sum:
# 			ans += cnt[(pre_s % 2)^1]
# 			# ans += 1 if pre_s % 2 == 1
# 			cnt[pre_s % 2] += 1
# 		return ans % (10 ** 9 + 7)

# class Solution:
#     def numOfSubarrays(self, arr):
#         s=[0]*(len(arr)+1)
#         for i,x in enumerate(arr):
#             s[i+1]=s[i]+x
#         mod=10**9+7
#         ans=0
#         cnt=[0]*2
#         for sj in s:
#             ans+=cnt[(sj%2)^1]
#             cnt[(sj%2)]+=1
#         return ans%mod

if __name__ == '__main__':
	arr = [1,4,4,5]
	cls = Solution1()
	print(cls.numOfSubarrays(arr))
	