from collections import defaultdict

class Solution1:
	def goodTriplets(self, nums1, nums2):
		def check_num(lis1, lis2, lis3):
			ans = 0
			if not lis1 or not lis2 or not lis3:
				return ans
			length1 = len(lis1)
			length2 = len(lis2)
			length3 = len(lis3)
			for k in range(length3 - 1, -1, -1):
				z = lis3[k]
				for j in range(length2 - 1, -1, -1):
					y = lis2[j]
					if y >= z:
						continue
					for i in range(length1 - 1, -1, -1):
						x = lis1[i]
						if x >= y:
							continue
						else:
							ans += i + 1
							break
			return ans


		nums2_dic = defaultdict(list)
		for i, x in enumerate(nums2):
			nums2_dic[x].append(i)
		n = len(nums1)
		result = 0
		for y in range(1, n - 1):
			y_2 = nums2_dic[nums1[y]]
			for x in range(0, y):
				x_2 = nums2_dic[nums1[x]]
				for z in range(y + 1, n):
					z_2 = nums2_dic[nums1[z]]
					result += check_num(x_2, y_2, z_2)
		return result
	
    
class Solution2:
	def goodTriplets(self, nums1, nums2):

		nums2_dic = defaultdict(int)
		for i, x in enumerate(nums2):
			nums2_dic[x] = i
		n = len(nums1)
		result = 0
		for y in range(1, n - 1):
			y_2 = nums2_dic[nums1[y]]
			for x in range(0, y):
				x_2 = nums2_dic[nums1[x]]
				for z in range(y + 1, n):
					z_2 = nums2_dic[nums1[z]]
					if x_2 < y_2 < z_2:
						result += 1
		return result



if __name__ == '__main__':
	nums1 = [2,0,1,3]
	nums2 = [0,1,2,3]
	print(Solution1().goodTriplets(nums1, nums2))