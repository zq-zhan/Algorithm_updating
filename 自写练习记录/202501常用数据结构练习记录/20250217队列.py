# 1.最近的请求次数
class RecentCounter:
	def __init__(self):
		self.queue = []

	def ping(self, t):
		self.queue.append(t)
		i = 0
		while self.queue[i] < t - 3000:
			i += 1
		return len(self.queue) - i
## 队列解法，因为pop(0)的复杂度是O(n)，需要移动后续元素向前填补空缺
class RecentCounter:
	def __init__(self):
		self.queue = deque()

	def ping(self, t):
		while self.queue and self.queue[0] < t - 3000:
			self.queue.popleft()
		self.queue.append(t)
		return len(self.queue)

# 2.按递增顺序显示卡牌
class Solution1:  # 双端队列
	def deckRevealedIncreasing(self, deck):
		deck.sort()
		ret = [0] * len(deck)
		index = deque(range(len(deck)))
		for i in sorted(deck):
			ret[index.popleft()] = i
			if index:
				index.append(index.popleft())
		return ret