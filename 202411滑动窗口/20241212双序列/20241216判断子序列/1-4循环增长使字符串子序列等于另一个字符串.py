# 4.循环增长使字符串子序列等于另一个字符串
class Solution1:
	def canMakeSubsequence(self,str1,str2):
		i = 0
		for x in str1:
			y = chr(ord(x)+1) if x != 'z' else 'a'
			if str2[i] == x or str2[i] == y:
				i += 1
				if i == len(str2):
					return True
		return False
	
if __name__ == '__main__':
	str1 = "om"
	str2 = "nm"
	cls = Solution1()
	print(cls.canMakeSubsequence(str1,str2))