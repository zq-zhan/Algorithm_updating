class Solution:
	def minimumTeachings(self, n, languages, friendships):
		st = set()
		for x, y in friendships:
			if not bool(set(languages[x - 1]) & set(languages[y - 1])):  # 判断交集是否有元素
				st.add(x - 1)
				st.add(y - 1)

		total = len(st)
		cnt = [0] * (n + 1)
		for x in st:
			for l in languages[x]:
				cnt[l] += 1
		return total - max(cnt)  # 减掉会的最多的语言的人次，其他人就得都学这个语言

if __name__ == '__main__':
	n = 3
	languages = [[2],[1,3],[1,2],[3]]
	friendships = [[1,4],[1,2],[3,4],[2,3]]
	print(Solution().minimumTeachings(n, languages, friendships))