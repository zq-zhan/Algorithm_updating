## 灵神题解——模拟长除法
class Solution:
	def fractionToDecimal(self, numerator, denominator):
		sign = '-' if numerator * denominator < 0 else ''
		numerator = abs(numerator)
		denominator = abs(denominator)

		q, r = divmod(numerator, denominator)  # 初始整数部分q和余数r
		if r == 0:
			return sign + str(q)

		ans = [sign + str(q) + '.']
		r_to_pos = {r:1}
		while r:
			q, r = divmod(r * 10, denominator)
			ans.append(str(q))
			if r in r_to_pos:
				pos = r_to_pos[r]
				return f"{''.join(ans[:pos])}({''.join(ans[pos:])})"
			r_to_pos[r] = len(ans)
		return ''.join(ans)

if __name__ == '__main__':
	s = Solution()
	print(s.fractionToDecimal(1, 2 ** 10 * 13))  # 0.5