# 1.判断子序列
class Solution1:
	def isSubsequence(self,s,t):
		p1 = p2 = 0
		n, m = len(s), len(t)
		while p1 < n and p2 < m:
			if t[p2]!=s[p1]:
				p2 += 1
			else:
				p1 += 1
				p2 += 1
		return True if p1 == n-1 else False
## 灵神思路
class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):  # 所有字符匹配完毕
                    return True  # s 是 t 的子序列
        return False

# 2.通过删除字母匹配到字典里最长的单词
class Solution1:
	def findLongestWord(self,s,dictionary):
		ans = ''
		for word in dictionary:
			p1 = p2 = 0
			n, m = len(s), len(word)
			while p1 < n and p2 < m:
				if s[p1] != word[p2]:
					p1 += 1
				else:
					p2 += 1
					p1 += 1

			if p2 == m:
				if p2 > len(ans):
					ans = word
				elif p2 == len(ans) and word < ans:
					ans = word
		return ans

# 3.追加字符以获得子序列
## 复杂度： O(m+n)
class Solution1: 
	def appendCharacters(self,s,t):
		p1 = p2 = 0
		n, m = len(s),len(t)
		while p1 < n and p2 < m:
			if s[p1] != t[p2]:
				p1 += 1
			else:
				p1 += 1
				p2 += 1
		return m - p2 
## 复杂度：O(n)
class Solution2:
	def appendCharacters(self,s,t):
		i = 0
		for x in s:
			if t[i] == x:
				i += 1
				if i == len(t):
					return 0
		return len(t) - i

# 4.循环增长使字符串子序列等于另一个字符串
class Solution1:
	def canMakeSubsequence(self,str1,str2):
		i = 0
		for x in str1:
			y = chr(ord(x)+1) if b != 'z' else 'a'
			if str2[i] == x or str2[i] == y:
				i += 1
				if i == len(str2):
					return True
		return False

# 5.驼峰式匹配
class Solution1:
	def camelMatch(self,queries,pattern):
		ans = [True] * len(queries)
		for i,substr in enumerate(queries):
			p1 = p2 = 0
			n, m = len(substr), len(pattern)
			while p1 < n or p2 < m:
				if p1 <n and p2 < m and substr[p1] == pattern[p2]:
					p1 += 1
					p2 += 1
				else:
					if p1 <n and substr[p1].islower():
						p1 += 1
					else:
						ans[i] = False
						break
		return ans

## 灵神思路
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(queries)
        #找不符合条件的case将对应ans置为false
        ans = [True] * n 

        for i,query in enumerate(queries):
            j  = 0
            for q in query:
                #两个置为false的条件
                #1、已经匹配到全部字符了但仍然有大写字母的
                #2、还没有匹配玩全部字符但是有不属于pattern的大写字母
                if (j== len(pattern) and q.isupper()) or (j < len(pattern) and q.isupper() and q != pattern[j] ):
                    ans[i] = False 
                    break
                #如果匹配到了则移动指针
                if j < len(pattern) and q == pattern[j]:
                    j+=1
            #循环完没有匹配完的也需要置为false
            if j< len(pattern):
                ans[i] =False
        return ans

# 6.找出与数组相加的整数2
## 理解为什么它可以成为一个判断子序列的问题
class Solution1:
	def minimumAddedInteger(self,nums1,nums2):
		nums1.sort(reverse=True)
		nums2.sort(reverse=True)
		ans = inf
		
		for i,c in enumerate(nums1):
			ori_diff = nums2[0] - c
			p1 = i 
			p2 = 0
			n, m = len(nums1), len(nums2)
			cnt_diffrent = 0
			cnt_same = 0
			while p1 < n and p2 < m:
				if nums2[p2] - nums1[p1] != ori_diff:
					cnt_diffrent += 1
					p1 += 1
					if cnt_diffrent > 2:
						break
				else:
					cnt_same += 1
					p1 += 1
					p2 += 1
			if cnt_same == m:
				ans = min(ans,ori_diff)
				break
		return ans
## 灵神题解
class Solution:
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        # 枚举保留 nums1[2] 或者 nums1[1] 或者 nums1[0]
        # 倒着枚举是因为 nums1[i] 越大答案越小，第一个满足的就是答案
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            # 在 {nums1[i] + x} 中找子序列 nums2
            j = 0
            for v in nums1[i:]:
                if nums2[j] == v + x:
                    j += 1
                    # nums2 是 {nums1[i] + x} 的子序列
                    if j == len(nums2):
                        return x
        # 题目保证答案一定存在
        return nums2[0] - nums1[0]

# 7.最长特殊序列
class Solution1:
	def findLUSlength(self,strs):
		p1 = p2 = 0
		while p1 < len(strs):
			words = strs[p1]
			while p2 < len(strs):
				if p2 == p1:
					p1 += 1
					continue
				




