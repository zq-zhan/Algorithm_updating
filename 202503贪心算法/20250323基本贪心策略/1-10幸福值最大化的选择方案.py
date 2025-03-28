class Solution1:
	def maximumHappinessSum(self, happiness, k):
		happiness.sort(reverse = True)
		cnt = 0
		ans = 0
		for x in happiness:
			if k > 0:
				ans += max(x - cnt,0)
				cnt += 1
				k -= 1
			else:
				break
		return ans
	
## 灵神题解
class Solution2:
	def maximumHappinessSum(self, happiness, k):
		happiness.sort(reverse = True)
		ans = 0
		for i, x in enumerate(happiness[:k]):
			if x <= i:
				break
			ans += x - i
		return ans
	
if __name__ == '__main__':
	happiness = [12,1,42]
	k = 3
	print(Solution1().maximumHappinessSum(happiness, k))