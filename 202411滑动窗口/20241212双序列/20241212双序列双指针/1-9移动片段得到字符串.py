from collections import Counter

# 9.移动片段得到字符串
# class Solution1:
# 	def canChange(self,start,target):
# 		target_dic={'L':[],'R':[]}
# 		for i in range(len(target)):
# 			if target[i]=='L':
# 				target_dic['L'].append(i)
# 			elif target[i]=='R':
# 				target_dic['R'].append(i)
# 			else:
# 				continue
# 		j = 0
# 		n = len(start)
# 		while j < n:
# 			cnt_L=0
# 			# cnt_R=len(target_dic['R'])-1
# 			while len(target_dic['L'])>0 and start[j] == 'L' and cnt_L<=len(target_dic['L']):
# 				if start[j-1] == '_' and j > target_dic['L'][cnt_L]:
# 					temp=start[j-1]
# 					start[j-1]=start[j]
# 					start[j]=temp
# 					j -= 1
# 					cnt_L += 1
# 				else:
# 					return False
# 		k = len(start)-1
# 		while k > 0:
# 			cnt_R=len(target_dic['R'])-1
# 			while len(target_dic['R'])>0 and start[k] == 'R' and cnt_R>=0:
# 				if start[k]==
# 				temp = start[k]
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

if __name__ == '__main__':
	# start = "_L__R__R_"
	# target = "L______RR"
	start="___L___"
	target="_L_____"
	cls = Solution3()
	print(cls.canChange(start,target))