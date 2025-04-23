from collections import Counter, defaultdict

# 20250420森林中的兔子
# class Solution1:
# 	def numRabbits(self, answers):
# 		answers = set(answers)
# 		ans = 0
# 		for x in answers:
# 			ans += x + 1
# 		return ans
	

# class Solution1:
# 	def numRabbits(self, answers):
# 		ans_dic = []
# 		ans = 0
# 		for x in answers:
# 			if x not in ans_dic or x == 0:
# 				ans += x + 1
# 				ans_dic.append(x)
# 		return ans

class Solution1:
	def numRabbits(self, answers):
		ans_dic = Counter(answers)
		ans = 0
		for key, cnt in ans_dic.items():
			# ans += ((cnt - 1) // (key + 1) + 1) * (key + 1)
			ans += (cnt + key) // (key + 1) * (key + 1)
		return ans
      
## 灵神题解
class Solution:
    def numRabbits(self, answers):
        ans = 0
        left = defaultdict(int)
        for x in answers:
            if left[x] == 0:
                ans += x + 1  # 找到了一个大小为 x+1 的颜色组
                left[x] = x  # 允许其他 x 只兔子也回答 x
            else:
                left[x] -= 1
        return ans
	
if __name__ == '__main__':
	# answers = [10,10,10]
	# answers = [1,0,1,0,0]
	answers = [0,0,1,1,1]
	print(Solution().numRabbits(answers))