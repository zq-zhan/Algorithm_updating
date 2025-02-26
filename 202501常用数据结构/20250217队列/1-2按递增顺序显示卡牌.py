# 2.按递增顺序显示卡牌
from collections import deque


class Solution1:  # 双端队列
	def deckRevealedIncreasing(self, deck):
		deck.sort()
		ret = [0] * len(deck)
		index = deque(range(len(deck)))
		for i in deck:
			ret[index.popleft()] = i
			if index:
				index.append(index.popleft())
		return ret
	
# 按递增顺序显示卡牌
class Solution2:
	def deckRevealedIncreasing(self, nums):
		nums.sort()
		index_lis = deque(range(len(nums)))

		ans = [0] * len(nums)
		for x in nums:
			ans[index_lis.popleft()] = x
			if index_lis:
				index_lis.append(index_lis.popleft())
		return ans
	
if __name__ == '__main__':
	deck = [17, 13, 11, 2, 3, 5, 7]
	print(Solution2().deckRevealedIncreasing(deck))