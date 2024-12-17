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

class Solution2:
	def camelMatch(self,queries,pattern):
		ans = [False]*len(queries)
		upper_patter=''
		for x in pattern:
			if x.isupper():
				upper_patter += x
		for j,substr in enumerate(queries):
			i = 0
			flag = 1
			for char in substr:
				if char.isupper() and (i > len(upper_patter) or char != upper_patter[i]):
					flag = 0
					break
				elif char.isupper() and char == upper_patter[i]:
					i += 1
			if flag:
				ans[j]=True
		return ans
	
## 灵神思路
class Solution3:
    def camelMatch(self, queries, pattern):
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

	
if __name__ == '__main__':
	queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
	pattern = "FoBa"
	s = Solution3()
	print(s.camelMatch(queries,pattern))