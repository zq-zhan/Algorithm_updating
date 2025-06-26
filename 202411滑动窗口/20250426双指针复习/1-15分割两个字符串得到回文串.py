class Solution1:
	def checkPalindromeFormation(self, a, b):
		pre_str_a = sub_str_a = pre_str_b = sub_str_b = ""
		left, right = 0, len(a) - 1
		while left < right:
			pre_str_a += a[left]
			sub_str_a += a[right]
			pre_str_b += b[left]
			sub_str_b += b[right]
			left += 1
			right -= 1
			if len(pre_str_a) > 1 and pre_str_a != sub_str_b and pre_str_b != sub_str_a:
				return False
		return True
	
class Solution:
    def checkPalindromeFormation(self, a, b):
        # 如果 a_prefix + b_suffix 可以构成回文串则返回 True，否则返回 False
        def check(a: str, b: str) -> bool:
            i, j = 0, len(a) - 1  # 相向双指针
            while i < j and a[i] == b[j]:  # 前后缀尽量匹配
                i += 1
                j -= 1
            s, t = a[i: j + 1], b[i: j + 1]  # 中间剩余部分
            return s == s[::-1] or t == t[::-1]  # 判断是否为回文串
        return check(a, b) or check(b, a)

if __name__ == '__main__':
	a = "pvhmupgqeltozftlmfjjde"
	b = "yjgpzbezspnnpszebzmhvp"
	print(Solution().checkPalindromeFormation(a, b))