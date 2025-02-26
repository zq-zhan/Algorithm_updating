# 5.设计浏览器历史记录
class BrowserHistory:
	def __init__(self, homepage):
		self.s = []
		self.s.append(homepage)
		self.cnt = 0
		# self.cnt += 1

	def visit(self, url):
		while len(self.s) != self.cnt + 1:  # 因为visit会删除浏览历史前进的记录
			self.s.pop()
		self.s.append(url)
		self.cnt += 1

	def back(self, steps):
		# if self.cnt - steps >= 0:
		# 	temp_cnt = self.cnt - steps
		# 	self.cnt -= steps
		# 	return self.s[temp_cnt]
		# else:
		# 	self.cnt = 0
		# 	return self.s[0]
		self.cnt = max(self.cnt - steps, 0)
		return self.s[self.cnt]

	def forward(self, steps):
		# if self.cnt + forward <= len(self.s) - 1:
		# 	temp_cnt = self.cnt + forward
		# 	self.cnt += forward
		# 	return self.s[temp_cnt]
		# else:
		# 	self.cnt = len(self.s) - 1
		# 	return self.s[-1]
		self.cnt = min(self.cnt + steps, len(self.s) - 1)
		return self.s[self.cnt]
		
if __name__ == '__main__':
	bh = BrowserHistory("leetcode.com")
	bh.visit("google.com")
	bh.visit("facebook.com")
	bh.visit("youtube.com")
	# bh.back(1)
	print(bh.back(1))
	print(bh.back(1))
	print(bh.forward(1))
	bh.visit("linkedin.com")
	print(bh.forward(2))
	print(bh.back(2))
	print(bh.back(7))