# 7.长按键入
class Solution1:
	def isLongPressedName(self,names,typed):
		p1 = p2 = 0
		n = len(names)
		m = len(typed)
		while p2 < m:
			while p1 < n:
				cnt_p1 = 0
				cnt_p2 = 0
				while p1 < n-1 and names[p1]==names[p1+1]:
					p1 += 1
					cnt_p1 += 1
					# continue
				while p2 < m-1 and typed[p2]==typed[p2+1]:
					p2 += 1
					cnt_p2 += 1
					# continue
				if names[p1] == typed[p2] and cnt_p2 >= cnt_p1:
					p1 += 1
					p2 += 1
				else:
					return False
			if p2 < m:
				return False
		return True

## 思路二：
class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        m, n = len(name), len(typed)

        while j < n:
            if i < m and j < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j >= 1 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == m
		
if __name__ == '__main__':
	# name="saeed"
	# typed="ssaaedd"
	name = "leelee"
	typed = "lleeelee"
	# name = "alex"
	# typed = "aaleexa"
	s = Solution2()
	print(s.isLongPressedName(name,typed))