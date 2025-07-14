# class Solution:
# 	def possibleStringCount(self, word):
# 		left = ans = 0
# 		word = word + word[-1] + '0'
# 		for right, c in enumerate(word):
# 			if c == word[left]:
# 				continue
# 			ans += right - left - 1
# 			left = right
# 		return ans
	
class Solution:
	def possibleStringCount(self, word):
		left = ans = 0
		word += '0'
		for right, c in enumerate(word):
			if c == word[left]:
				continue
			ans += right - left - 1
			left = right
		return ans + 1  # 都不犯错


if __name__ == '__main__':
	word = "abbccccdd"
	print(Solution().possibleStringCount(word))