# 4.删除字符使字符串变好
# class Solution1:
# 	def makeFancyString(self,s):
# 		ans = 0
# 		left, right = 0, 1
# 		while right < len(s):
# 			if s[right] != s[left]:
# 				if right - left >= 3:
# 					ans += right - left - 2
# 				left = right
# 			right += 1
# 		if right - left >= 3:
# 			ans += right - left - 2
# 		return ans

class Solution1:
	def makeFancyString(self,s):
		ans = ''
		left, right = 0, 1
		while right < len(s):
			if s[right] != s[left]:
				if right - left >= 2:
					ans += s[left] * 2
				else:
					ans += s[left]
				left = right
			right += 1
		if right - left >= 2:
			ans += s[left] * 2
		else:
			ans += s[left]
		return ans
	

# 灵神思路
class Solution2:
    def makeFancyString(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            start = i
            c = s[i]
            while i < n and c == s[i]:
                if (i-start+1) <3:
                    ans.append(s[i])
                i += 1
        return "".join(ans)

class Solution:
	def makeFancyString(self, s):
		n = len(s)
		s += '0'
		ans = temp_s = ''
		for i in range(n):
			temp_s += s[i]
			if s[i] == s[i + 1]:
				continue
			ans += temp_s[:2]
			temp_s = ''
		return ans

if __name__ == '__main__':
	s = "leeetcode"
	cls = Solution2()
	print(cls.makeFancyString(s))