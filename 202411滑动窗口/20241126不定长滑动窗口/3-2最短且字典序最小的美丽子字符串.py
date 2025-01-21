from collections import Counter
# 最短且字典序最小的美丽子字符串
class Solution1:
	def shortestBeautifulSubstring(self,s,k):
		n=len(s)
		dic_win=Counter()
		left=0
		substr_lis=[]
		len_result=n+1
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_win['1']==k:
				substr_lis.append(s[left:right+1])
				len_result=min(len_result,right-left+1)
				dic_win[s[left]]-=1
				left+=1
		substr_lis.sort()
		return substr_lis[-1] if len_result<=n else ''

## 方法二：灵神
class Solution2:
	def shortestBeautifulSubstring(self,s,k):
		if s.count('1')<k:
			return ''
		ans=s
		cnt1=left=0
		# bea_str=[]
		for right,c in enumerate(s):
			cnt1+=int(c)
			while cnt1>=k:
				if cnt1==k:
					temp_str=s[left:right+1]
					if len(temp_str)<len(ans) or (len(temp_str)==len(ans) and temp_str<ans):
						ans=temp_str
						# bea_str.append(temp_str)
				cnt1-=int(s[left])
				left+=1
		# bea_str.sort()
		return ans
	
# 优化
class Solution3:
	def shortestBeautifulSubstring(self,s,k):
		if s.count('1')<k:
			return ''
		ans=s
		cnt1=left=0
		# bea_str=[]
		for right,c in enumerate(s):
			cnt1+=int(c)
			while cnt1==k:
				# if cnt1==k:
				temp_str=s[left:right+1]
				if len(temp_str)<len(ans) or (len(temp_str)==len(ans) and temp_str<ans):
					ans=temp_str
					# bea_str.append(temp_str)
				cnt1-=int(s[left])
				left+=1
		# bea_str.sort()
		return ans

class Solution_re:
	def shortestBeautifulSubstring(self,s,k):
		ans=s+'1'
		left=cnt_1=0
		# result_substr=s
		for right,c in enumerate(s):
			cnt_1+=int(c)
			while cnt_1==k:
				temp_str=s[left:right+1]
				if len(temp_str)<len(ans) or (len(temp_str)==len(ans) and temp_str<ans):
					ans=temp_str
				cnt_1-=int(s[left])
				left+=1
		return ans if len(ans)<=len(s) else ''

# 2.最短且字典序最小的美丽子字符传
class Solution1:
	def shortestBeautifulSubstring(self, s, k):
		ans = s + '0'
		left = 0
		substr_cnt = 0
		for right, c in enumerate(s):
			substr_cnt += 1 if c == '1' else 0
			while substr_cnt == k:
				if len(ans) > right - left + 1 or (len(ans) == right - left + 1 and ans > s[left:right+1]):
					ans = s[left:right + 1]
				substr_cnt -= 1 if s[left] == '1' else 0
				left += 1
		return ans if len(ans) <= len(s) else ''
	

if __name__=='__main__':
	s="11000111"
	k=3
	cls=Solution1()
	print(cls.shortestBeautifulSubstring(s,k))