# 2.哪种连续子字符串更长
class Solution1:
	def checkZeroOnes(self,s):
		long_1 = 0
		long_0 = 0
		left, right = 0, 1
		while right < len(s):
			if s[right] != s[left]:
				if s[left] == '0':
					long_0 = max(long_0, right - left)
					left = right
				else:
					long_1 = max(long_1, right - left)
					left = right
			right += 1
		if s[left] == '0':
			long_0 = max(long_0, right - left)
			left = right
		else:
			long_1 = max(long_1, right - left)
			left = right
		return long_1 > long_0
	
class Solution2:
    def checkZeroOnes(self, s):
        mx0 = mx1 = cnt = 0
        prev = '#'   
        for ch in s:
            if prev == ch:
                cnt += 1
            else:
                if prev == '0':
                    mx0 = max(mx0, cnt)
                elif prev == '1':
                    mx1 = max(mx1, cnt)
                cnt = 1
            prev = ch
        if prev == '0':
            mx0 = max(mx0, cnt)
        elif prev == '1':
            mx1 = max(mx1, cnt)
        return mx1 > mx0

if __name__ == '__main__':
	s = "111000"
	print(Solution2().checkZeroOnes(s))
	