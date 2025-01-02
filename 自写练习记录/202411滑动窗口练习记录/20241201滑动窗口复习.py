# 定长滑动窗口
## 定长子串中元音的最大数目
### 错误点：if判断条件错误
class Solution:
	def maxVowels(self,s,k):
		ans=cnt=0
		for i,c in enumerate(s):
			cnt+=1 if c in "aeiou" else 0
			if i <= k-1:
				continue
			ans=max(ans,cnt)
			cnt-=1 if s[i-k+1] in "aeiou" else 0
		return ans
## 子数组最大平均数
### 错误点：ans初始化错误
class Solution:
	def findMaxAverage(self,nums,k):
		ans=float('-inf')
		total=0
		for i,c in enumerate(nums):
			total+=c 
			if i<k-1:
				continue
			ans=max(ans,total)
			total-=nums[i-k+1]
		return ans/k
## 大小为K且平均值大于等于阈值的子数组数目
class Solution:
	def numOfSubarrays(self,arr,k,threshold):
		ans=0
		total=0
		for i,c in enumerate(arr):
			total+=c
			if i<k-1:
				continue
			if total/k>=threshold:
				ans+=1
			total-=arr[i-k+1]
		return ans

# 不定长滑动窗口——求最长/最大
## 1.无重复字符的最小子串
### 自写版
class Solution_rv:
	def lengthOfLongestSubstring(self,s):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(s):
			dic_win[c]+=1
			while max(dic_win.values())>1:
				dic_win[s[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return ans
class Solution_rv2:
	def lengthOfLongestSubstring(self,s):
		ans=left=0
		win_lis=[]
		for right,c in enumerate(s):
			while c in win_lis:
				win_lis=win_lis[1:]
				left+=1
			win_lis.append(c)
			ans=max(ans,right-left+1)
		return ans
### 灵神逻辑
class Solution:
	def lengthOfLongestSubstring(self,s):
		ans=left=0
		window=set()
		for right,c in enumerate(s):
			while c in window:
				window.remove(s[left])
				left+=1
			window.add(c)
			ans=max(ans,right-left+1)
		return ans
## 2.每个字符最多出现两次的最长子字符串
class Solution_rv:
	def maximumLengthSubstring(self,s):
		ans=left=0
		dic_win=defaultdict(int)
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_win[c]>2:
				dic_win[s[left]]-=1
				left+=1
			ans=max(ans,right-left+1)
		return ans
## 3.删掉一个元素以后全为1的最长子数组
class Solution_rv:
	def longestSubarray(self,nums):
		ans=left=0
		cnt_0=0
		for right,c in enumerate(nums):
			cnt_0+=(1-c)
			while cnt_0>1:
				cnt_0-=(1-nums[left])
				left+=1
			ans=max(ans,right-left+1)
		return ans


# 不定长滑动数组——求最短/最小
## 长度最小的子数组
class Solution_re:
	def minSubArrayLen(self,target,nums):
		ans=len(nums)
		left=0
		total=0
		for right,c in enumerate(nums):
			total+=c
			while total>=target:
				total-=nums[left]
				ans=min(ans,right-left+1)
				left+=1
		return ans if ans<len(nums) else 0
## 最短且字典序最小的美丽子字符串
class Solution_re:
	def shortestBeautifulSubstring(self,s,k):
		ans=s+'1'
		left=cnt_1=0
		# result_substr=s
		for right,c in enumerate(s):
			cnt_1+=int(c)
			while cnt_1>=k:
				if cnt_1==k:
					temp_str=s[left:right+1]
					if len(temp_str)<len(ans) or (len(temp_str)==len(ans) and temp_str<ans):
						ans=temp_str
				cnt_1-=int(s[left])
				left+=1
		return ans if len(ans)<=len(s) else ''
### 灵神
class Solution:
	def shortestBeautifulSubstring(self,s,k):
		if s.count('1')<k:
			return ''
		ans=s
		cnt_1=left=0
		for right,c in enumerate(s):
			cnt_1+=int(c)
			while cnt_1>k or s[left]=='0':
				cnt_1 -= int(s[left])
				left+=1
			if cnt_1==k:
				temp_str=s[left:right+1]
				if len(temp_str)<len(ans) or (len(temp_str)==len(ans) and temp_str<ans):
					ans=temp_str
		return ans

