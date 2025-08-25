EPS = 1e-9
class Solution:
	def judgePoint24(self, cards):
		n = len(cards)
		if n == 1:
			return abs(cards[0] - 24) < EPS

		for i, x in enumerate(cards):
			for j in range(i + 1, n):
				y = cards[j]
				candidates = [x + y, x - y, y - x, x * y]
				if abs(y) > EPS:  # 分母不为0
					candidates.append(x / y)
				if abs(x) > EPS:
					candidates.append(y / x)

				new_cards = cards[:j] + cards[j + 1:]
				for res in candidates:
					new_cards[i] = res
					if self.judgePoint24(new_cards):
						return True
		return False
	
if __name__ == '__main__':
	cards = [4,1,8,7]
	print(Solution().judgePoint24(cards))