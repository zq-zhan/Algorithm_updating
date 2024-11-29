# 方法一：递归
class ListNode:
	def __init(self,value=0,next=None):
		self.val=value
		self.next=next

class Solution:
	def addTwoNumbers(self,l1,l2,carry=0):
		if l1 is None and l2 is None:
			return ListNode(carry) is carry else None  # 如果进位了就创建值为carry的节点
		if l1 is None:
			l1,l2=l2,l1  # 交换，简化代码
		s=carry+l1.val+l2.val
		l1.val=s%10
		l1.next=self.addTwoNumbers(l1.next,l2.next if l2 else None,s//10)
		return l1



# 方法二：迭代
class Solution:
	def addTwoNumbers(l1,l2):
		dummy_node=ListNode(0)
		current=dummy_node
		carry=0
		while l1 or l2 or carry:
			if l1 is None:
				l1=ListNode(0)
			if l2 is None:
				l2=ListNode(0)
			s=carry+l1.val+l2.val
			l1=l1.next
			l2=l2.next
			carry=s//10
			current.next=ListNode(s%10)
			current=current.next
		return dummy_node.next

class Solution:
	def addTwoNumbers(l1,l2):
		cur=dummy=ListNode()
		carry=0
		while l1 or l2 or carry:
			if l1:
				carry +=l1.val
				l1=l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			cur.next=ListNode(carry%10)
			carry //= 10
		return dummy.next

def create_linked_list_from_list(lis):
	head=ListNode(0)
	current=head
	for value in lis:
		current.next=ListNode(value)
		current=current.next
	return head.next


# 单链表的读取
class GetLinkElem():
	def get_link_elem(l1,i):
		k=1
		p=l1
		while p and k<i:
			p=p.next
			k+=1
		if p is None or k>i:
			print("错误")
		return p.val


# 最长不重复连续子字符串
## 方法一：哈希表+滑动窗口
class Solution():
	def getLongestSubstring(self,s):
		dict={}
		i=-1
		res=0
		for j in range(len(s)):
			if s[j] not in dict:
				dict[s[j]]=j
			res=max(res,j-i)
			i=max(dict[s[j]],i)
		return res
## 方法二：暴力解法
class Solution2():
	def getLongestSubstring(self,s):
		res=1
		for length in range(2,len(s)):
			for i in range(len(s)):
				string=s[i,i+length]
				dict={}
				flag=True
				for char in string:
					if char in dict:
						flag=False
						break
					dict[char]=1
				if flag:
					res=max(res,length)
					break
		return res
## 方法三：动态规划+哈希表
class Solution3():
	def getLongestSubstring(self,s):
		i,dict,temp,res=-1,{},0,0
		for j in range(len(s)):
			if s[j] not in dict:
				dict[s[j]]=j
			i=max(dict[s[j]],i)
			if j-i>temp:
				tmp=temp+1
			else:
				tmp=j-i
			res=max(res,tmp)
		return res

class Solution3():
	def getLongestSubstring(self,s):
		dic={}
		res=tmp=0
		for j in range(len(s)):
			i=dic.get(s[j],-1)  # 获取最近的相同字符索引
			dic[s[j]]=j  # 更新哈希表
			tmp=tmp+1 if tmp<j-i else j-i
			res=max(res,tmp)
		return res




# 滑动窗口题单
## 1.定长子串中最大元音数
class Solution():
	def maxVowels(self,s,k):
		ans,vowels=0,0
		for i in range(len(s)):
			if s[i] in "aeiou":
				vowels+=1
			if i<k-1:
				continue
			ans=max(ans,vowels)
			if s[i-k+1] in "aeiou":
				vowels-=1
		return ans

## 2.子数组最大平均数
### 方法一：自写版
class Solution1():
	def findMaxAverage(self,nums,k):
		ans,sum_k=[],0
		for i in range(len(nums)):
			sum_k+=nums[i]
			if i < k-1:	
				continue
			ans=ans.append(sum_k/k)
			sum_k-=nums[i-k+1]
		return max(ans)
### 方法二：灵神滑动窗口
class Solution2():
	def findMaxAverage(self,nums,k):
		ans=float("-inf")
		total=0
		for i,c in enumerate(nums):
			total+=c
			if i < k-1:
				continue
			ans=max(ans,total)
			total-=nums[i-k+1]
		return ans
### 方法三：非套路，但简洁版
class Solution3():
	def findMaxAverage(self,nums,k):
		max_sum,total=sum(nums[0:k]),sum(nums[0:k])
		for i in range(k,len(nums)):
			total+=nums[i]-nums[i-k]
			max_sum=max(max_sum,total)
		return max_sum/k


## 3.大小为K且平均值大于等于阈值的子数组数目
### 方法一：自写版：
class Solution():
	def numOfSubarrays(self,arr,k,threshold):
		# ans=float("-inf")
		total=0
		cnt=0
		for i,c in enumerate(arr):
			total+=c
			if i < k-1:
				continue
			# ans=max(ans,total/k)
			if total/k >= threshold:
				cnt+=1
			total-=arr[i-k+1]
		return cnt



## 4.半径为k的子数组平均值
### 方法一：自写版
class Solution1():
	def getAverages(self,nums,k):
		avgs=[]
		# total=0
		for i in range(len(nums)):
		    if i < k or i > len(nums)-k-1:
		        avgs.append(-1)
		        continue
		    total=sum(nums[i-k:i+k+1])
		    avgs.append(int(total/(2*k+1)))
		return avgs
### 方法二：滑动窗口
class Solution2():
	def getAverages(self,nums,k):
		avgs=[-1]*len(nums)
		total=0
		for i,c in enumerate(nums):
			total+=c
			if i < 2*k:
				continue
			avgs[i-k]=int(total/(2*k+1))
			total-=nums[i-2*k]
		return avgs


## 5.得到K个黑块的最少涂色次数
### 方法一：自写版
class Solution1():
	def minimumRecolors(self,blocks,k):
		w_cnt=0
		ans=float('inf')
		for i,c in enumerate(blocks):
			if c == 'w':
				w_cnt+=1
			if i < k-1:
				continue
			ans=min(ans,w_cnt)
			if blocks[i-k+1]=='w':
				w_cnt-=1
		return ans
### 方法二：灵神自写滑动窗口版
class Solution2():
	def minimumRecolors(self,blocks,k):
		cnt_w=ans=blocks[:k].count('W')
		for in_,out in zip(blocks[k:],blocks):  #注意这里进出数组的选取！
			cnt_w+=(in_ == 'W') - (out == 'W')
			ans=min(ans,cnt_w)
		return ans

## 6.爱生气的书店老板
### 方法一：自写版
class Solution1():
    def maxSatisfied(self, customers, grumpy, minutes):
        ans = 0
        for i in range(len(customers)):
            ans += customers[i] * (1 - grumpy[i])
        total = ans
        temp = 0
        for i, c in enumerate(customers):
            temp = c if grumpy[i] == 1 else 0
            total += temp
            if i < minutes - 1:
                continue
            ans = max(ans, total)
            temp=customers[i-minutes+1] if grumpy[i-minutes+1]==1 else 0
            total-=temp
        return ans  # 添加返回值
### 方法二：灵神滑动窗口
class Solution2():
	def maxSatisfied(self,customers,grumpy,minutes):
		s=[0,0]  # 老板不生气时的顾客之和+老板生气时的顾客滑动窗口内和
		total=0
		for i,(c,g) in enumerate(zip(customers,grumpy)):
			s[g]+=c
			if i < minutes-1:
				continue
			total=max(total,s[1])
			if grumpy[i-minutes+1]:
				s[1]-=customers[i-minutes+1]
		return s[0]+total

## 7.字符串是否包含所有长度为k的二进制子串
### 方法一：自写版
class Solution1():
	def hasAllCodes(self,s,k):
		cnt=tmp=0
		dic={}
		true_num=2**k
		for i in range(len(s)-k+1):
			dic[s[i:i+k]]=i
		if len(dic.keys())<true_num:
			return False
		else:
			return True


## 8.几乎唯一子数组的最大和
### 方法一：自写版
class Solution1():
	def maxSum(self,nums,m,k):
		ans=0
		for i in range(len(nums)-k+1):
			substr=nums[i:i+k]
			if len(set(substr))>=m:
				ans=max(ans,sum(substr))
			else:
				continue
		return ans
### 方法二：灵神滑动窗口
class Solution2():
	def maxSum(self,nums,m,k):
		ans=0
		total=sum(nums[:k-1])
		cnt_dic=Counter(nums[:k-1])
		for in_,out in zip(nums[k-1:],nums):
			total+=in_
			cnt_dic[in_]+=1
			if len(cnt_dic)>=m:
				ans=max(ans,total)
			cnt_dic[out]-=1
			if cnt_dic[out]==0:
				del cnt_dic[out]
			total-=out
		return ans
			

## 9.长度为K子数组中的最大和
### 方法一：自写版
class Solution1():
	def maximumSubarraySum(self,nums,k):
		ans=total=0
		cnt_lis=Counter()
		for i,c in enumerate(nums):
			total+=c
			cnt_lis[c]+=1
			if i < k-1:
				continue
			if len(cnt_lis)>=k:
				ans=max(ans,total)
			cnt_lis[nums[i-k+1]]-=1
			if cnt_lis[nums[i-k+1]]==0:
				del cnt_lis[nums[i-k+1]]
			total-=nums[i-k+1]
		return ans


## 10.可获得的最大点数
class Solution():
	def maxScore(self,cardPoints,k):
		s=[0,len(cardPoints)-1]
		ans=total=0
		for i,c in enumerate(cardPoints):
			total+=max(s[0],s[1])
			if cardPoints[s[0]]>cardPoints[s[1]]:
				s[0]+=1
			else:
				s[1]-=1
### 方法一：逆向思维-拿走的最大点数和=剩下的连续子串最小点数
class Solution1():
	def maxScore(self,cardPoints,k):
		ans=float("inf")
		new_len=len(cardPoints)-k
		total=0
		for i,c in enumerate(cardPoints):
			if new_len<=0:
				ans=min(ans,total)
				break
			total+=c
			if i < new_len-1:
				continue
			ans=min(ans,total)
			total-=cardPoints[i-new_len+1]
		return sum(cardPoints)-ans
### 方法二：逆向思维
class Solution2():
	def maxScore(self,cardPoints,k):
		new_len=len(cardPoints)-k
		ans=total=sum(cardPoints[:new_len])
		for i in range(new_len,len(cardPoints)):
			total+=cardPoints[i]-cardPoints[i-new_len]
			ans=min(ans,total)
		return sum(cardPoints)-ans
### 方法三：正向思维-动态规划、滑动窗口
class Solution3():
	def maxScore(self,cardPoints,k):
		ans=total=sum(cardPoints[:k-1])
		for i in range(1,k+1):
			total+=cardPoints[-i]-cardPoints[k-i]  # 加上进的数、减去出的数
			ans=max(ans,total)
		return ans
### 方法四：正向思维-滑动窗口(有误)
class Solution4():
	def maxScore(self,cardPoints,k):
		ans=total=0
		new_arr=cardPoints[-k:]+cardPoints[:k]
		for i,val in enumerate(cardPoints):
			total+=val
			if i < k-1:
				continue
			ans=max(ans,total)
			total-=cardPoints[i-k+1]
		return ans



## 11.拆炸弹
### 方法一：自写版
class Solution1():
	def decrypt(self,code,k):
		res_lis=[]
		total=0
		new_len=abs(k)
		if k>0:
			new_arr=code[1:len(code)+1]+code
		elif k<0:
			new_arr=code[-new_len:]+code
		else:
			return [0]*len(code)
		cnt=0
		for i,c in enumerate(new_arr):
			total+=c
			if i < new_len-1:
				continue
			res_lis.append(total)
			cnt+=1
			total-=new_arr[i-new_len+1]
			if cnt==len(code):
				break
		return res_lis
### 方法二：灵神滑动窗口
class Solution2():
	def decrypt(self,code,k):
		ans=[0]*len(code)
		r=k+1 if k >0 else n
		k=abs(k)
		n=len(code)
		total=sum(code[r-k,r])
		for i in range(n):
			ans[i]=total
			total+=code[r%n]-code[(r-k)%n]
			r+=1
		return ans
##
class Solution3():
	def decrypt(self,code,k):
		n=len(code)
		ans=[0]*n
		r=k+1 if k>0 else n
		k=abs(k)
		total=sum(code[r-k:r])
		for i in range(n):
			ans[i]=total
			total+=code[r%n]-code[(r-k)%n]
			r+=1
		return ans


## 12.子串的最大出现次数
### 方法一：自写版
class Solution1():
	def maxFreq(self,s,maxLetters,minSize,maxSize):
		dic=Counter()
		ans=0
		substr=''
		k=minSize
		for i,c in enumerate(s):
			substr+=c
			if i < k-1:
				continue
			if len(set(substr))<=maxLetters:
				dic[substr] = dic.get(substr,0) + 1
			substr=substr[1:]
		if dic:
			return max(dic.values())
		else:
			return 0

## 12.滑动子数组的美丽值
### 方法一：自写版，超出时间限制
class Solution1():
	def getSubarrayBeauty(self,nums,k,x):
		ans_lis=[]
		substr_lis=[]
		for i,c in enumerate(nums):
			substr_lis.append(c)
			if i < k-1:
				continue
			sort_lis=sorted(substr_lis)
			if sort_lis[x-1]<0:
				ans_lis.append(sort_lis[x-1])
			else:
				ans_lis.append(0)
			substr_lis=substr_lis[1:]
		return ans_lis
### 方法二：灵神,滑动窗口+暴力枚举
class Solution2():
	def getSubarrayBeauty(self,nums,k,x):
		cnt_lis=[0]*101
		for c in nums[:k-1]:
			cnt_lis[c]+=1
		ans_lis=[0]*(len(nums)-k+1)
		for i,(in_,out) in enumerate(zip(nums[k-1:],nums)):
			cnt_lis[in_]+=1
			left=x
			for j in range(-50,0):
				left -= cnt_lis[j]
				if left <= 0:
					ans_lis[i]=j
					break
			cnt_lis[out] -= 1
		return ans_lis


# 不定长滑动窗口
## 求最长、最大
### 1、无重复字符的最长子串
##### 方法一：自写版
class Solution1():
	def lengthOfLongestSubstring(self,s):
		ans=0
		dic={}
		substr=''
		for i,c in enumerate(s):
			if c not in substr:
				substr+=c
				dic[substr]+=1
				continue
			ans=max(ans,len(substr))
			substr=substr[1:]+c
		return ans

# 水果成篮
## 方法一：自写版
class Solution1():
	def totalFruit(self,fruits):
		ans=left=0
		window=Counter()
		for right,c in enumerate(fruits):
			# if c not in window:
			window[c]+=1
			while len(window)>2:
				if window[fruits[left]]>1:
					window[fruits[left]]-=1
				else:
					del window[fruits[left]]
				left += 1
			ans = max(ans,right-left+1)
		return ans

# 删除子数组的最大得分
## 方法一：自写版
class Solution1():
	def maximumUniqueSubarray(self,nums):
		ans=left=0
		total=0
		window=set()
		for right,c in enumerate(nums):
			# window.add(c)
			while c in window:
				window.remove(nums[left])
				total-=nums[left]
				left += 1
			window.add(c)
			total+=c
			ans = max(ans,total)
		return ans

# 最多 K 个重复元素的最长子数组
## 方法一：自写版
class Solution1():
	def maxSubarrayLength(self,nums,k):
		ans=left=0
		window=Counter()
		for right,c in enumerate(nums):
			window[c]+=1
			while window[c]>k:
				window[nums[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return ans

# 数组的最大美丽值
## 方法一：自写版
class Solution1():
	def maximumBeauty(self,nums,k):
		ans=left=0
		window=Counter()
		for right,c in enumerate(nums):
			for j in range(c-k,c+k+1):
				window[j]+=1
			while c not in window:
				for x in range(nums[left]-k,nums[left]+k+1):
					window[x] -= 1
				left += 1
			ans
## 方法二：排序+滑动窗口
class Solution2():
	def maximumBeauty(self,nums,k):
		num=nums.sort()
		ans=left=0
		for right,c in enumerate(nums):
			while c-nums[left]>2*k:
				left += 1
			ans=max(ans,right-left+1)
		return ans


# 最大连续1的个数
class Solution1():
	def longestOnes(self,nums,k):
		ans=left=0
		cnt_0=0
		for right,c in enumerate(nums):
			cnt_0 += 1 if c==0 else 0
			while cnt_0>k:
				cnt_0 -= 1 if nums[left]==0 else 0
				left += 1
			ans = max(ans,right-left+1)
		return ans


# 将x减到0的最小操作数
## 方法一：逆向思维
class Solution1():
	def minOperations(self,nums,k):
		ans=-1
		left=0
		total_win=0
		total=sum(nums)
		target_num=total-k
		if target<0:
			return -1
		for right,c in enumerate(nums):
			total_win+=c
			while total_win>target_num:
				total_win -= nums[left]
				left += 1
			if total_win==target_num:
				# cnt+=1
				ans=max(ans,right-left+1)
		if ans!=-1:
			return len(nums)-ans
		else:
			return -1
## 方法二：双指针
class Solution2():
	def minOperations(self,nums,x):
		s,n=0,len(nums)
		right=n
		while right and s+nums[right-1]<=x:  # 计算最长后缀
			right-=1
			s+=nums[right]
		if right==0 and s<x: return -1  # 全部移除也无法满足x的情况
		ans=n-right if s==x else inf
		for left,num in enumerate(nums):
			s+=


# 最高频元素的频数
## 方法一：自写版
class Solution1():
	def maxFrequency(self,nums,k):
		ans=left=0
		dic_win=Counter()
		max_record=0
		cnt=0
		for right,c in enumerate(nums):
			dic_win[c]+=1
			max_record=max(max_record,c)
			if max_record!=c:
				for temp in dic_win
				cnt+=(max_record-temp)*dic_win[temp] 
			while len(dic_win)>=2 and 

# 方法二：滑动窗口的转换视角
class Solution1():
	def maxFrequency(self,nums,k):
		# nums.sort()
		nums=sorted(nums)
		ans=left=0
		total=0
		for right,c in enumerate(nums):
			total+=c
			while c*(right-left+1)>total+k:
				total-=nums[left]
				left +=1
			ans=max(ans,right-left+1)
		return ans


# 每种字符至少取K个
## 方法一：自写版，逆向思维
class Solution1():
	def takeCharacters(self,s,k):
		ans=left=0
		dic_all=Counter(s)
		dic_win=Counter()
		if any(dic_all[c]<k for c in 'abc'):
			return -1
		for right,c in enumerate(s):
			dic_win[c]+=1
			# while dic_all['a']-dic_win['a']<k or dic_all['b']-dic_win['b']<k or dic_all['c']-dic_win['c']<k:
			while dic_all[c]-dic_win[c]<k:
				dic_win[s[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return len(s)-ans
## 方法二：灵神滑动窗口
class Solution2():
	def takeCharacters(self,s,k):
		ans=left=0
		dic_all=Counter(s)
		if any(dic_all[c]<k for c in 'abc'):
			return -1
		for right,c in enumerate(s):
			dic_all[c] -= 1
			while dic_all[c] < k:
				dic_all[s[left]] += 1
				left += 1
			ans = max(ans,right-left+1)
		return len(s)-ans

# 找出最长等值子数组
## 方法一：自写版
class Solution1:
	def longestEqualSubarray(self,nums,k):
		ans=left=0
		cnt=0
		all_dic=Counter(nums)
		win_lis=[]
		tmp=0
		for x in all_dic:
			if all_dic[x]>tmp:
				char=x
				tmp=all_dic[x]
		for right,c in enumerate(nums):
			while c!=char:
				left+=1
## 方法二：灵神滑动窗口思路
class Solution2:
	def longestEqualSubarray(self,nums,k):
		group_dic={}
		for i,c in enumerate(nums):
			if c in group_dic:
				group_dic[c].append(i-len(group_dic[c]))
			else:
				group_dic[c]=[i]
		ans=0
		for c in group_dic:
			if len(group_dic[c])<=ans:
				continue
			left=0
			c_lis=group_dic[c]
			for right,x in enumerate(c_lis):
				while x-c_lis[left]>k:
					left += 1
				ans=max(ans,right-left+1)
		return ans
## 方法三：灵神滑动窗口版
class Solution3:
    def longestEqualSubarray(self, nums, k):
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans




