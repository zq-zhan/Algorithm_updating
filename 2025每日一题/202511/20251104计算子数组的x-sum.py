from collections import defaultdict

class Solution:
	def findXSum(self, nums, k, x):
		temp_dic = defaultdict(int)
		ans = []
		for i, num in enumerate(nums):
			temp_dic[num] += 1
			if sum(temp_dic.values()) < k:
				continue
			else:
				new_arr = [(cnt, key) for key, cnt in temp_dic.items()]
				new_arr.sort(reverse = True)
				temp_s = 0
				for j in range(min(x, len(new_arr))):
					temp_s += new_arr[j][0] * new_arr[j][1]
				ans.append(temp_s)
				temp_dic[nums[i - k + 1]] -= 1	
		return ans		



if __name__ == '__main__':
	nums = [1,1,2,2,3,4,2,3]
	k = 6
	x = 2
	print(Solution().findXSum(nums, k, x))