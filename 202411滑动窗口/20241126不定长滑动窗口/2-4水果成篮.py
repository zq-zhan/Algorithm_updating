from collections import Counter, defaultdict
# 水果成篮
## 方法一：自写版
class Solution1():
	def totalFruit(self,fruits):
		ans=left=0
		window=Counter()
		for right,c in enumerate(fruits):
			# if c not in window:
			window[c]+=1
			while len(window)>2:
				if window[fruits[left]]>1:
					window[fruits[left]]-=1
				else:
					del window[fruits[left]]
				left += 1
			ans = max(ans,right-left+1)
		return ans
	
class Solution2:
	def totalFruit(self, fruits):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(fruits):
			dic_win[c] += 1
			while len(dic_win) > 2:
				if dic_win[fruits[left]] == 1:
					del dic_win[fruits[left]]
				else:
					dic_win[fruits[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

if __name__ == '__main__':
	fruits = [3,3,3,1,2,1,1,2,3,3,4]
	s = Solution2() 
	print(s.totalFruit(fruits))