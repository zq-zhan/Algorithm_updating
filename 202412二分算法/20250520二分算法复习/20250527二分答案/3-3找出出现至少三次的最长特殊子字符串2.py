from collections import defaultdict

class Solution1:
	def maximumLength(self, s):
		def check(target):
			dic_win = defaultdict(int)
			for i in range(n - target + 1):
				temp_s = s[i:i + target]
				dic_win[temp_s] += 1
			return max(dic_win.values()) >= 3

		n = len(s)
		left, right = 0, n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

## 灵神题解
class Solution2:
	def maximumLength(self, s):
		groups = defaultdict(list)
		cnt = 0
		for i, x in enumerate(s):
			cnt += 1
			if i + 1 == len(s) or x != s[i + 1]:
				groups[x].append(cnt)
				cnt = 0

		ans = 0
		for val in groups.values():
			val.sort(reverse = True)
			val.extend([0, 0])
			ans = max(ans, val[0] - 2, min(val[0] - 1, val[1]), val[2])
		return ans if ans else -1

# 二分法
class Solution3:  # O((n + m)log n) m为字符集大小
	def check(self, s, mid):
		mid_dic = defaultdict(int)
		n = len(s)
		left = 0
		while left < n:
			right = left + 1
			while right < n and s[right] == s[right - 1]:
				right += 1
			if right - left >= mid:
				mid_dic[s[left:left + mid]] += max(0, right - left - mid + 1)
			# mid_dic[s[left]] += max(0, right - left - mid + 1)  # 优化,字符串小于mid的话，right - left - mid + 1 为负数，不影响对符合特殊子串的计数
				if max(mid_dic.values()) >= 3:
					return True
			left = right
		return False

	def maximumLength(self, s):
		left, right = -1, len(s)
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(s, mid):
				left = mid
			else:
				right = mid
		return left if left > 0 else -1
	

class Solution4:  # O((n + m)log n) m为字符集大小
	# def check(self, s, mid):
	# 	mid_dic = defaultdict(int)
	# 	n = len(s)
	# 	left = 0
	# 	while left < n:
	# 		right = left + 1
	# 		while right < n and s[right] == s[right - 1]:
	# 			right += 1
	# 		if right - left >= mid:
	# 			mid_dic[s[left:left + mid]] += max(0, right - left - mid + 1)
	# 		# mid_dic[s[left]] += max(0, right - left - mid + 1)  # 优化,字符串小于mid的话，right - left - mid + 1 为负数，不影响对符合特殊子串的计数
	# 			if max(mid_dic.values()) >= 3:
	# 				return True
	# 		left = right
	# 	return False

	def maximumLength(self, s):
		def check(target):
			target_dic = defaultdict(int)
			ans = left = 0
			for right in range(1, len(s)):
				if right > 0 and s[right] == s[right - 1]:
					continue
				if right - left >= mid:
					temp_str = s[left:left + target]
					target_dic[temp_str] += max(0, right - left - mid + 1)
					if target_dic[temp_str] >= 3:
						return True
				left = right
			return False

		left, right = -1, len(s)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left if left > 0 else -1

if __name__ == '__main__':
	s = "aaaa"
	print(Solution4().maximumLength(s))