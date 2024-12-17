# 1.最小公共值
class Solution1:
	def getCommon(self,nums1,nums2):
		# ans=inf
		i=0
		j=0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				i+=1
			elif nums1[i] > nums2[j]:
				j+=1
			else:
				# ans=nums1[i]
				return nums1[i]
				# break
		return -1
## 灵神思路
class Solution2:
	def getCommon(self,nums1,nums2):
		j,m=0,len(nums2)
		for x in nums1:
			while j<m and nums2[j]<x:
				j+=1
			if j<m and nums2[j]==x:
				return x
		return -1

# 2.合并两个有序数组
class Solution1:
	def merge(self,nums1,m,nums2,n):
		i = m - 1 
		j = n - 1 
		k=m + n - 1
		while k >= 0:
			if i >= 0 and j >= 0:
				if nums2[j] > nums1[i]:
					nums1[k] = nums2[j]
					k -= 1
					j -= 1
				elif nums2[j] < nums1[i]:
					nums1[k] = nums1[i]
					i -= 1
					k -= 1
				else:
					nums1[k], nums1[k-1] = nums1[i], nums2[j]
					k -= 2
					i -= 1
					j -= 1
			elif i < 0:
				nums1[k] = nums2[j]
				j -= 1
				k -= 1
			else:
				nums1[k] = nums1[i]
				i -= 1
				k -= 1
		return nums1 
## 灵神思路
class Solution2:
	def merge(self,nums1,m,nums2,n):
		p1, p2, p = m-1, n-1, m+n-1
		while p2 >= 0:
			if p1 >= 0 and nums1[p1] > nums2[p2]:
				nums1[p] = nums1[p1]
				p1 -= 1
			else:
				nums1[p] = nums2[p2]
				p2 -= 1
			p -= 1
		return nums1

# 3.合并两个二维数组-求和法
class Solution1:
	def mergeArrays(self,nums1,nums2):
		p1 = p2 =0
		n = len(nums1)
		m = len(nums2)
		ans = []
		while p1 < n or p2 < m:
			if p1 < n and p2 < m:
				if nums1[p1][0] < nums2[p2][0]:
					ans.append([nums1[p1][0],nums1[p1][1]])
					p1 += 1
				elif nums1[p1][0] == nums2[p2][0]:
					ans.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
					p1 += 1
					p2 += 1
				else:
					ans.append([nums2[p2][0],nums2[p2][1]])
					p2 += 1
			elif p1 >= n:
				ans.append([nums2[p2][0],nums2[p2][1]])
				p2 += 1
			else:
				ans.append([nums1[p1][0],nums1[p1][1]])
				p1 += 1
		return ans
## 优化
class Solution1:
	def mergeArrays(self,nums1,nums2):
		p1 = p2 =0
		n = len(nums1)
		m = len(nums2)
		ans = []
		while p1 < n and p2 < m:
			if nums1[p1][0] < nums2[p2][0]:
				ans.append(nums1[p1])
				p1 += 1
			elif nums1[p1][0] == nums2[p2][0]:
				nums1[p1][1] += nums2[p2][1]
				ans.append(nums1[p1])
				p1 += 1
				p2 += 1
			else:
				ans.append(nums2[p2])
				p2 += 1
		if p1 < n:
			ans.extend(nums1[p1:])
		if p2 < m:
			ans.extend(nums2[p2:])
		return ans
## 灵神思路
class Solution2:
	def mergeArrays(self,nums1,nums2):
		ans = []
		i, n = 0, len(nums1)
		j, m = 0, len(nums2)
		while True:
			if i == n:
				ans.extend(nums2[j:])
				return ans
			if j == m:
				ans.extend(nums1[i:])
				return ans
			if nums1[i][0] < nums2[j][0]:
				ans.append(nums1[i])
				i += 1
			elif nums1[i][0] > nums2[j][0]:
				ans.append(nums2[j])
				j += 1
			else:
				nums1[i][1] += nums2[j][1]
				ans.append(nums1[i])
				i += 1
				j += 1

# 4.早餐组合
## 时间复杂度较大
class Solution1:
	def breakfastNumber(self,staple,drink,x):
		staple.sort()
		drink.sort()
		n = len(staple)
		m = len(drink)
		p1, p2 = n-1, n-1
		ans=0
		while p1 >= 0:
			while p2 >= 0:
				if staple[p1] + drink[p2] <= x:
					ans += (p2+1)
					break
				p2 -= 1
			p1 -= 1
		return ans
## O(nlogn)
class Solution2:
	def breakfastNumber(self,staple,drink,x):
		staple.sort()
		drink.sort()
		n = len(staple)
		m = len(drink)
		p1, p2 = 0, m-1
		ans=0
		while p1 < n and p2 >=0:
			if staple[p1]+drink[p2]<=x:
				ans += (p2+1)
				p1 += 1
			else:
				p2 -= 1
		return ans%(1000000007)

# 5.下标对中的最大距离
class Solution1:
	def maxDistance(self,nums1,nums2):
		# nums2.sort()
		n = len(nums1)
		m = len(nums2)
		p1 = n-1
		p2 = m-1
		ans = 0
		while p1 > p2:
			p1 -= 1
		while p1 >= 0:
			while p2 >= p1:
				if nums1[p1] <= nums2[p2]:
					ans = max(ans,p2-p1) 
					p1 -= 1
				else:
					p2 -= 1
					# p1 -= 1
			p1 -= 1
		return ans
## 思路二：
class Solution2:
	def maxDistance(self,nums1,nums2):
		n,m = len(nums1),len(nums2)
		ans = 0
		right =0
		for left in range(n):
			right = max(left,right)
			while right < m and nums2[right] >= nums1[left]:
				right += 1
			ans = max(ans,right-left)
		return ans
## 思路三：
class Solution3:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        l, r = 0, 0
        res = 0
        while l < m and r < n:
            while r < n and nums2[r] >= nums1[l]:
                res = max(res, r - l)
                r += 1
            l += 1
        
        return res

class Solution1:
	def maxDistance(self,nums1,nums2):
		# nums2.sort()
		n = len(nums1)
		m = len(nums2)
		p1 = n-1
		p2 = m-1
		ans = 0
		while p1 > p2:
			p1 -= 1
		while p1 >= 0 and p2 >=0
			if nums1[p1] <= nums2[p2]:
				ans = max(ans,p2-p1) 
				p1 -= 1
			else:
				p2 -= 1
					# p1 -= 1
			# p1 -= 1
		return ans

# 6.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		p1 = p2 = 0
		n = len(arr1)
		m = len(arr2)
		ans = 0
		while p1 < n:
			while p2 < m:
				if arr1[p1] - arr2[p2] > d:
					p2 += 1
				elif arr1[p1] - arr2[p2] < -d:
					ans += 1
					break
				else:
					break
			if p2 == m:
				ans += n-p1
				break
			p1 += 1
		return ans
## 灵神思路
class Solution2:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		ans = j =0
		for x in arr1:  # p1和p2两个指针不能同时循环
			while j < len(arr2) and arr2[j] < x - d:
				j += 1
			if j == len(arr2) or arr2[j] > x + d:
				ans += 1
		return ans



# 7.长按键入
class Solution1:  # 有误
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
class Solution:
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
##
class Solution:
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

# 9.移动片段得到字符串
class Solution1:
	def canChange(self,start,target):
		target_dic={'L':[],'R':[]}
		for i in range(len(target)):
			if target[i]=='L':
				target_dic['L'].append(i)
			elif target[i]=='R':
				target_dic['R'].append(i)
			else:
				continue
		j = 0
		n = len(start)
		while j < n:
			cnt_L=0
			# cnt_R=len(target_dic['R'])-1
			while len(target_dic['L'])>0 and start[j] == 'L' and cnt_L<=len(target_dic['L']):
				if start[j-1] == '_' and j > target_dic['L'][cnt_L]:
					temp=start[j-1]
					start[j-1]=start[j]
					start[j]=temp
					j -= 1
					cnt_L += 1
				else:
					return False
		k = len(start)-1
		while k > 0:
			cnt_R=len(target_dic['R'])-1
			while len(target_dic['R'])>0 and start[k] == 'R' and cnt_R>=0:
				if start[k]==
				temp = start[k]
## 灵神思路
class Solution2:
	def canChange(sef,start,target):
		if start.replace('_', '') != target.replace('_', ''):
			return False
		p1=p2=0
		n=len(start)
		m=len(target)
		while p1<n and p2<m:
			if start[p1]=='_':
				p1+=1
			if target[p2]=='_':
				p2+=1
			if p1 < n and p2 <m and start[p1]==target[p2]=='L' and p1<p2:
				return False
			if p1 < n and p2 <m and start[p1]==target[p2]=='R' and p1>p2:
				return False
			if p1 < n and p2 <m and start[p1]==target[p2]:
				p1+=1
				p2+=1
		return True

class Solution3:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == '_':
                continue
            while target[j] == '_': 
                j += 1
            if i != j and (c == 'L') == (i < j):
                return False
            j += 1
        return True

# 10.在LR字符串中交换相邻字符
class Solution1:  # 未充分理解题意
	def canTransform(self,start,result):
		start_dic=Counter(start)
		result_dic=Counter(result)
		if start_dic != result_dic:
			return False
		i = 0
		j = 0 
		while i < len(start)-1:
			while start[i]==result[j+1] and start[i+1]==result[j] and (start[i]=='X' or start[i+1]=='X'):
				j += 2
				i += 2
			if start[i]==result[j]:
				i += 1
				j += 1
			else:
				return False
		return True
## 灵神思路
class Solution2:
	def canTransform(self,start,result):
		if start.replace('X','')!=result.replace('X',''):
			return False
		j = 0
		for i,c in enumerate(start):
			if start[i] == 'X':
				continue
			while result[j]=='X':
				j += 1
			if i!=j and (c == 'L') == (i < j):
				return False
			j += 1
		return True

# 11.比较含退格的字符串
class Solution1:
	def backspaceCompare(self,s,t):
		s = list(s)
		t = list(t)
		n = len(s)
		m = len(t)
		p1, p2 = n-1 ,m-1
		while p1 > 0:
			while p1 >= 0 and s[p1] != '#':
				p1 -= 1
				continue
			cnt = 0
			while p1 >= 0 and s[p1] == '#':
				cnt += 1
				s[p1] = ''
				p1 -= 1
			s[p1-cnt+1:p1+1]=['']*cnt
		while p2 > 0:
			while p2 >= 0 and t[p2] != '#':
				p2 -= 1
				continue
			cnt = 0
			while p2 >= 0 and t[p2] == '#':
				cnt += 1
				t[p2] = ''
				p2 -= 1
			t[p2-cnt+1:p2+1]=['']*cnt
		return s==t
class Solution2:
	def backspaceCompare(self,s,t):
		n = len(s)
		m = len(t)
		p1, p2 = n-1 ,m-1
		cnt1 = 0
		cnt2 = 0
		while p1 >= 0 or p2 >= 0:
			while p1 >= 0:
				if s[p1] == '#':
					cnt1 += 1
					p1 -= 1
				elif cnt1 > 0:
					cnt1 -= 1
					p1 -= 1
				else:
					break
			while p2 >= 0:
				if t[p2] == '#':
					cnt2 += 1
					p2 -= 1
				elif cnt2 > 0:
					cnt2 -= 1
					p2 -= 1
				else:
					break
			if p1 >= 0 and p2 >= 0:
				if s[p1] != t[p2]:
					return False
			elif p1 >=0 or p2 >= 0:
				return False
			p1 -= 1
			p2 -= 1
		return True

# 12.区间列表的交集
class Solution1:
	def intervalIntersection(self,firstList,secondList):
		n, m = len(firstList), len(secondList)
		# if len(firstList)==0 or len(secondList)==0:
		# 	return []
		p1 = p2 = 0
		ans = []
		while p1 < n and p2 < m:
			if firstList[p1][1] < secondList[p2][0]:
				p1 += 1
				continue
			elif firstList[p1][0] > secondList[p2][1]:
				p2 += 1
				continue
			else:
				# temp_list=[]
				if firstList[p1][1] < secondList[p2][1]:
					max_p1_num = max(firstList[p1][0],secondList[p2][0])
					# for i in range(max_p1_num,firstList[p1][1]+1):
					# 	temp_list.append(i)
					ans.append([max_p1_num,firstList[p1][1]])
					p1 += 1
				else:
					max_p1_num = max(firstList[p1][0],secondList[p2][0])
					# for i in range(max_p1_num,secondList[p2][1]):
					# 	temp_list.append(i)
					ans.append([max_p1_num,secondList[p2][1]])
					p2 += 1
		return ans
## 优化
class Solution2:
	def intervalIntersection(self,firstList,secondList):
		p1 = p2 = 0
		n, m = len(firstList),len(secondList)
		ans = []
		while p1 < n and p2 < m:
			a1, a2 = firstList[p1][0],firstList[p1][1]
			b1, b2 = secondList[p2][0], secondList[p2][1]
			if a1 <= b2 and a2 >= b1:
				ans.append(max(a1,b1),min(a2,b2))
			if b2 < a2:
				p2 += 1
			else:
				p1 += 1
		return ans

# 13.最小差
class Solution1:
	def smallestDifference(self,a,b):
		a.sort()
		b.sort()
		p1 = p2 = 0
		n, m = len(a), len(b)
		ans = inf
		while p1 < n and p2 < m:
			ans = min(ans,abs(a[p1]-b[p2]))
			if a[p1] - b[p2] < 0:
				p1 += 1
			else:
				p2 += 1
		return ans

# 14.最大得分
class Solution1:
	def maxSum(self,nums1,nums2):
		p1 = p2 = 0
		n, m = len(nums1), len(nums2)
		ans = 0
		total_p1 = 0
		total_p2 = 0
		i = j = 0
		same_lis = []
		while i < n and j < m:
			if nums1[i] < nums2[j]:
				i += 1
			elif nums1[i] > nums2[j]:
				j += 1
			else:
				same_lis.append(nums1[i])
				i += 1
				j += 1
		k = 0
		# latest_point = 0
		while p1 < n or p2 < m:
			if p1 < n:
				if k == len(same_lis):
					total_p1 += nums1[p1]
					p1 += 1
				elif nums1[p1] < same_lis[k]:
					total_p1 += nums1[p1]
					p1 += 1
			if p2 < m:
				if k == len(same_lis):
					total_p2 += nums2[p2]
					p2 += 1
				elif nums2[p2] < same_lis[k]:
					total_p2 += nums2[p2]
					p2 += 1
			flag = 0

			if p1 < n and p2 < m and nums1[p1] == nums2[p2]:
				ans += max(total_p1+same_lis[k],total_p2+same_lis[k])
				total_p1 = 0
				total_p2 = 0
				k += 1
				flag = 1
				p1 += 1
				p2 += 1
		

		if flag:
			ans += max(total_p1, total_p2)
		return ans
## 简洁优化版
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        sum1 = 0
        sum2 = 0
        while i < n1 or j < n2:
            if (i < n1) and (j >= n2 or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            elif (j < n2) and (i >= n1 or nums1[i] > nums2[j]):
                sum2 += nums2[j]
                j += 1
            else:
                sum1 = sum2 = max(sum1,sum2) + nums1[i]
                i += 1
                j += 1

        return int(max(sum1,sum2) % (1e9+7))

