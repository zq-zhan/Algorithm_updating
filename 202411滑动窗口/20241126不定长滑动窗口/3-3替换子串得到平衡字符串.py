from collections import Counter

# 替换子串得到平衡字符串
## 方法一：自写版
class Solution1:
	def balancedString(self,s):
		ans=len(s)+1
		left=0
		target_num=len(s)//4
		dic_all=Counter(s)
		if len(dic_all)==4 and min(dic_all.values())==target_num:
			return 0
		for right,c in enumerate(s):
			dic_all[c]-=1
			while max(dic_all.values())<=target_num:
				dic_all[s[left]]+=1
				ans=min(ans,right-left+1)
				left += 1
		return ans 

if __name__ == '__main__':
	s = "QQQW"
	print(Solution1().balancedString(s))