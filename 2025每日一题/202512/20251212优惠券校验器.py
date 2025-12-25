class Solution:
	def validateCoupons(self, code, businessLine, isActive):
		n = len(code)
		temp_lis = []
		for i in range(n):
			if isActive[i] and businessLine[i] in ('electronics', 'grocery', 'pharmacy', 'restaurant')\
				and code[i] != '' and all(x.isalpha() or x.isdigit() or x == '_' for x in code[i]):
				temp_lis.append((businessLine[i], code[i]))
		temp_lis.sort()
		return [y for _, y in temp_lis]
	
if __name__ == '__main__':
	code = ["SAVE20","","PHARMA5","SAVE@20"]
	businessLine = ["restaurant","grocery","pharmacy","restaurant"]
	isActive = [True, True, True, True]
	print(Solution().validateCoupons(code, businessLine, 'true'))