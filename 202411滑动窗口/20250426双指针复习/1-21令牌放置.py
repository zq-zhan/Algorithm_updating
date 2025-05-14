class Solution1:
	def bagOfTokensScore(self, tokens, power):
		tokens.sort()
		ans = temp_ans = 0
		left, right = 0, len(tokens) - 1
		while left <= right:
			if power >= tokens[left]:
				temp_ans += 1
				ans = max(ans, temp_ans)
				power -= tokens[left]
				left += 1
			elif temp_ans > 0:
				temp_ans -= 1
				power += tokens[right]
				right -= 1
			else:
				return ans
		return ans
	
if __name__ == '__main__':
	tokens = [100,200,300,400]
	power = 200
	print(Solution1().bagOfTokensScore(tokens, power))