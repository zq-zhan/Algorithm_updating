
# 6.找出与数组相加的整数2
from math import inf


class Solution1:
	def minimumAddedInteger(self,nums1,nums2):
		nums1.sort(reverse=True)
		nums2.sort(reverse=True)
		ans = inf
		
		for i,c in enumerate(nums1):
			ori_diff = nums2[0] - c
			p1 = i 
			p2 = 0
			n, m = len(nums1), len(nums2)
			cnt_diffrent = 0
			cnt_same = 0
			while p1 < n and p2 < m:
				if nums2[p2] - nums1[p1] != ori_diff:
					cnt_diffrent += 1
					p1 += 1
					if cnt_diffrent > 2:
						break
				else:
					cnt_same += 1
					p1 += 1
					p2 += 1
			if cnt_same == m:
				ans = min(ans,ori_diff)
				break
		return ans
	
## 灵神题解
class Solution2:
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        # 枚举保留 nums1[2] 或者 nums1[1] 或者 nums1[0]
        # 倒着枚举是因为 nums1[i] 越大答案越小，第一个满足的就是答案
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            # 在 {nums1[i] + x} 中找子序列 nums2
            j = 0
            for v in nums1[i:]:
                if nums2[j] == v + x:
                    j += 1
                    # nums2 是 {nums1[i] + x} 的子序列
                    if j == len(nums2):
                        return x
        # 题目保证答案一定存在，所以不需要执行i = 0 的情况
        return nums2[0] - nums1[0]
	
	
if __name__ == '__main__':
	nums1 = [4,6,3,1,4,2,10,9,5]
	nums2 = [5,10,3,2,6,1,9]
	cls = Solution2()
	print(cls.minimumAddedInteger(nums1,nums2))