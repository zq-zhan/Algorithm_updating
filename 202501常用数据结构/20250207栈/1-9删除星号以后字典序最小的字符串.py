# import chain


## 灵神思路一
# class Solution1:
# 	def clearStars(self, s):
# 		ans_lis = [[] for _ in range(26)]
# 		start_a = ord('a')
# 		for i, c in enumerate(s):
# 			if c != '*':
# 				ans_lis[ord(c) - start_a].append(i)
# 				continue
# 			for p in ans_lis:
# 				if p:
# 					p.pop()
# 					break
# 		return ''.join(s[i] for i in sorted(chain.from_iterable(ans_lis)))
	
# 思路二：
class Solution2:
    def clearStars(self, s):
        s = list(s)
        st = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                st[ord(c) - ord('a')].append(i)
                continue
            for p in st:
                if p:
                    s[p.pop()] = '*'
                    break
        return ''.join(c for c in s if c != '*')


if __name__ == '__main__':
	s = 'aaba*'
	print(Solution2().clearStars(s))