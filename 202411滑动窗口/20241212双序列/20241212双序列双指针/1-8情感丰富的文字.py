from collections import Counter

# 8.情感丰富的文字
class Solution1:
	def expressiveWords(self,s,words):
		n = len(s)
		ans = 0
		for substr in words:
			p1 = p2 = 0
			m = len(substr)
			while p1 < n:
				while p2 < m:
					if substr[p2]==s[p1]:
						p1 += 1
						p2 += 1
					else:
						p1 = n+1
						break
					cnt_p1=1
					cnt_p2=1
					while p1<n and s[p1]==s[p1-1]:
						p1 += 1
						cnt_p1 += 1
					while p2<m and substr[p2]==substr[p2-1]:
						p2 += 1
						cnt_p2 += 1
					if cnt_p1==cnt_p2 or cnt_p1>=3:
						continue
					else:
						p1 = n+1
						break
				if p1 < n and p2 >= m:
					break
			if p1 == n:
				ans += 1
		return ans

class Solution2:
    def expressiveWords(self, s, words):
        n = len(s)
        # 预处理获得重复字符个数
        cnt = [1]*n
        for i in range(1,n):
            if s[i] == s[i-1]:
                cnt[i] += cnt[i-1]
        for i in range(n-2,-1,-1):
            if s[i] == s[i+1]:
                cnt[i] = cnt[i+1]

        def check(s,t):
            n,m = len(s),len(t)
            if n < m:
                return False 
            i = j = 0
            while i < n:
                if j < m and s[i] == t[j]:
                    i += 1;j += 1
                elif i >= 1 and s[i] == s[i-1] and cnt[i] >= 3: # 关键判断，相比之前的 925. 长按键入 多一行代码
                    i += 1
                else:
                    return False
            return i == n and j == m
        
        return sum(1 for t in words if check(s,t))


# 情感丰富的文字self_practice
class Solution3:
	def expressiveWords(self,s,words):
		s_cnt=[1]*len(s)
		for i in range(1,len(s)):
			if s[i]==s[i-1]:
				s_cnt[i]+=s_cnt[i-1]
		for j in range(len(s)-2,-1,-1):
			if s[j]==s[j+1]:
				s_cnt[j]=s_cnt[j+1]
		# 不能用Counter()，因为s中可能有同样的字符出现在不同位置而非连续的3个以上
		def check(s,t,s_dic):
			p1 = p2 = 0
			n, m = len(s), len(t)
			if n < m:
				return False
			while p1 < n:
				if p2 < m and s[p1] == t[p2]:  # 注意这里要将p2<m放在循环外面，否则会漏掉最后一个字符
					p1 += 1
					p2 += 1
				elif p1 > 0 and s[p1] == s[p1-1] and s_cnt[p1]>=3:
					p1 += 1
				else:
					return False
			return p1 == n and p2 == m
		return sum(1 for t in words if check(s,t,s_cnt))


if __name__ == '__main__':
	s = "heeellooo"
	words = ["hello", "hi", "helo"]
	cls = Solution3()
	print(cls.expressiveWords(s,words))