# 3.找出出现至少三次的最长特殊子字符串2
## 滑动窗口解法
from collections import defaultdict,Counter


class Solution1:  # 错解
	def maximumLength(self, s):
		left, right = 0, 1
		n = len(s)
		ans = -1
		while left < n and right < n:
			if s[right] == s[right - 1]:
				right += 1
				continue
			if right - left >= 3:
				ans = max(ans, right - left - 2)
			left = right
			right += 1
		if right - left >= 3:
			ans = max(ans, right - left - 2)
		return ans
	
# 二分法
class Solution2:  # O((n + m)log n) m为字符集大小
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
	
## 灵神思路——贪心
class Solution3:
	def maximumLength(self, s):
		groups = defaultdict(list)
		cnt = 0
		for i, ch in enumerate(s):
			cnt += 1
			if i + 1 == len(s) or ch != s[i + 1]:
				groups[ch].append(cnt)  # 统计连续字符的长度
				cnt = 0

		ans = 0
		for a in groups.values():
			a.sort(reverse = True)
			a.extend([0, 0])
			ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

		return ans if ans else -1

if __name__ == '__main__':
	s = "ereerrrererrrererre"
	cls = Solution2()
	print(cls.maximumLength(s))