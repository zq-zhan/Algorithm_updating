# 8.不含AAA或BBB的字符串
class Solution1:
	def strWithout3a3b(self, a, b):
		ans = ''
		while a > 0 or b > 0:
			if a == b:
				ans += 'ab'
				a -= 1
				b -= 1
			elif a > b and b > 0:
				ans += 'aab'
				a -= 2
				b -= 1
			elif a < b and a > 0:
				ans += 'bba'
				a -= 1
				b -= 2
			elif a == 0:
				ans += 'b' * b
				b = 0
			elif b == 0:
				ans += 'a' * a
				a = 0
		return ans


##
class Solution2:
    def strWithout3a3b(self, A, B):
        if A == B:
            return "ab" * A

        ans = ""

        la = A
        lb = B

        while la > 0 and lb > 0:
            if la > lb:
                ans += "aab"
                la -= 2
                lb -= 1
            elif la < lb:
                ans += "bba"
                la -= 1
                lb -= 2
            else:
                if A > B:
                    ans += "ab" * la
                else:
                    ans += "ba" * la
                la = 0
                lb = 0
        if A > B:
            ans += "a" * la + "b" * lb
        else:
            ans += "b" * lb + "a" * la

        return ans

if __name__ == '__main__':
	a = 4
	b = 1
	print(Solution2().strWithout3a3b(a, b))