# 越长越合法
## 统计最大元素出现至少K次的子数组
class Solution1:
	def countSubarrays(self,nums,k):
		ans=left=0
		max_data=max(nums)
		cnt=0
		for right,c in enumerate(nums):
			if c==max_data:
				cnt+=1
			while cnt>=k:
				cnt-=1 if nums[left]==max_data else 0
				left+=1
			ans+=left
		return ans
### 思路2
class Solution2:
	def countSubarrays(self,nums,k):
		ans=left=0
		n=len(nums)
		mx=max(nums)
		cnt=0
		for right,c in enumerate(nums):
			if c==mx:
				cnt+=1
			while cnt>=k:
				ans+=n-right
				if nums[left]==mx:
					cnt-=1
				left+=1
		return ans

## 字符至少出现K次的子字符串
class Solution1:
	def numberOfSubstrings(self,s,k):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(s):
			dic_win[c]+=1
			while max(dic_win.values())>=k:
				dic_win[s[left]]-=1
				left+=1
			ans+=left
		return ans
### 灵神思路:影响while条件判断的只有c因为只有c的值会增加，所以无需max
class Solution2:
	def numberOfSubstrings(self,s,k):
		ans=left=0
		dic_win=defaultdict(int)
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_win[c]>=k:
				dic_win[s[left]]-=1
				left+=1
			ans+=left
		return ans

## 统计完全子数组的数目
class Solution1:
	def countCompleteSubarrays(self,nums):
		ans=left=0
		dic_all=Counter(nums)
		dic_win=Counter()
		n=len(dic_all)
		for right,c in enumerate(nums):
			dic_win[c]+=1
			while len(dic_win)==n:
				if dic_win[nums[left]]==1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]]-=1
				left+=1
			ans+=left
		return ans

## 统计好子数组的数目
class Solution1:
	def countGood(self,nums,k):
		ans=left=0
		total=0
		dic_win=Counter()
		for right,c in enumerate(nums):
			dic_win[c]+=1
			if dic_win[c]>=2:
				total+=dic_win[c]*(dic_win[c]-1)/2
			while total>=k:
				# if dic_win[s[left]]==1:
				# 	del dic_win
				total-=(dic_win[nums[left]]-1) if dic_win[nums[left]]>=2 else 0
				dic_win[nums[left]]-=1
				left+=1
			ans+=left
		return ans

## 统计重新排列后包含另一个字符串的子字符串数目
class Solution1:
	def validSubstringCount(self,word1,word2):
		ans=left=0
		dic_win=Counter()
		dic_word2=Counter(word2)
		for right,c in enumerate(word1):
			if c in dic_word2:
				dic_word2[c]-=1
			while max(dic_word2.values())<=0:
				if word1[left] in dic_word2:
					dic_word2[word1[left]]+=1
				left+=1
			ans+=left
		return ans
### 灵神思路（类同3-6最小覆盖子串的思路！！！）
class Solution2:
	def validSubstringCount(self,s,t):
		if len(word1)<len(t):
			return 0
		dic_word2=Counter(t)
		less=len(dic_word2)  # 串口中有less个字母的出现次数比t少
		ans=left=0
		for b in s:
			cnt[b]-=1
			if cnt[b]==0:
				less-=1
			while less==0:
				if cnt[s[left]]==0:
					less+=1
				cnt[s[left]]+=1
				left+=1
			ans+=left
		return ans

# 越短越合法
## 乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self,nums,k):
		ans=left=0
		plus_total=1
		if k>=1:
			return 0
		for right,c in enumerate(nums):
			plus_total*=c
			while plus_total>=k:
				plus_total/=nums[left]
				left+=1
			ans+=right-left+1
		return ans
## 统计满足k约束的子字符串数量
class Solution1:
	def countKConstraintSubstrings(self,s,k):
		ans=left=0
		dic_win={0:0,1:1}
		for right,c in enumerate(s):
			dic_win[c]+=1
			while max(dic_win.values())>k:
				dic_win[s[left]]-=1
				left+=1
			ans+=right-left+1
		return ans
## 不间断子数组
class Solution1:
	def continuousSubarrays(self,nums):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(nums):
			dic_win[c]+=1
			while max(dic_win.keys())-min(dic_win.keys())>2:
				if dic_win[nums[left]]==1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]]-=1
				left+=1
			ans+=right-left+1
		return ans

