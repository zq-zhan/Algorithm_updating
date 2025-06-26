from collections import defaultdict

class Solution:
	def findLongestSubarray(self, array):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		mx_ans = pre_s = 0
		temp_index = len(array)
		ans = []
		for i, x in enumerate(array):
			pre_s += 1 if x.isalpha() else -1
			target = dic_win.get(pre_s, i)
			if target == i:
				dic_win[pre_s] = i
			else:
				if i - dic_win[pre_s] > mx_ans or \
					(i - dic_win[pre_s] == mx_ans and dic_win[pre_s] < temp_index):
					mx_ans = i - dic_win[pre_s]
					ans = array[dic_win[pre_s] + 1:i + 1]
					temp_index = dic_win[pre_s]
		return ans
	
if __name__ == '__main__':
	array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
	print(Solution().findLongestSubarray(array))