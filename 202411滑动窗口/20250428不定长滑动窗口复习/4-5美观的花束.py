from collections import defaultdict

class Solution1:
	def beautifulBouquet(self, flowers, cnt):
		dic_win = defaultdict(int)
		ans = left = 0
		mod = 10 ** 9 + 7
		for right, c in enumerate(flowers):
			dic_win[c] += 1
			while max(dic_win.values()) > cnt:
				dic_win[flowers[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans 
	
if __name__ == '__main__':
	flowers = [1,2,3,2]
	cnt = 1
	print(Solution1().beautifulBouquet(flowers, cnt))