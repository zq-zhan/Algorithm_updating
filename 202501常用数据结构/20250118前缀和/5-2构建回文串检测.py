# 2.构建回文串检测
class Solution1:
	def canMakePaliQueries(self, s, queries):
		sum = [[0] * 26]
		for c in s:
			sum.append(sum[-1].copy())
			sum[-1][ord(c) - ord('a')] += 1

		ans = []
		for left, right, k in queries:
			m = 0
			for sl, sr in zip(sum[left], sum[right + 1]):
				m += (sr - sl) % 2
			ans.append(m // 2 <= k)
		return ans

class Solution:
    def canMakePaliQueries(self, s, queries):
        sum = [0]
        for c in s:
            bit = 1 << (ord(c) - ord('a'))  # 将1向左移动ord(c) - ord('a')位，得到该字母对应的比特位
            sum.append(sum[-1] ^ bit)  # 该比特对应字母的奇偶性：奇数变偶数，偶数变奇数

        ans = []
        for left, right, k in queries:
            m = (sum[left] ^ sum[right + 1]).bit_count()
            ans.append(m // 2 <= k)
        return ans


if __name__ == '__main__':
	s = "abcda"
	queries = [[3, 3, 0], [1, 2, 0], [0, 2, 1], [0, 3, 1]]
	print(Solution1().canMakePaliQueries(s, queries)) # Output: [true, false, false, true]