# 20250111——求出数字答案
class Solution1:
	def generateKey(self, nums1, nums2, nums3):
		nums1 = str(nums1)
		nums2 = str(nums2)
		nums3 = str(nums3)
		nums1 = (4 - len(nums1)) * '0' + nums1
		nums2 = (4 - len(nums2)) * '0' + nums2
		nums3 = (4 - len(nums3)) * '0' + nums3
		ans = '0'
		for i in range(4):
			char = min(nums1[i], nums2[i], nums3[i])
			if i == 0 and char > '0':
				ans += char
			elif i > 0:
				ans += char
		return ans[1:] if len(ans) > 1 else ans
## 字符串解法
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        num1 ="0"*(4-len(num1))+num1
        num2 = "0"*(4-len(num2))+num2
        num3 = "0"*(4-len(num3))+num3

        ans = []
        for i in range(4):
            ans.append(str(min(int(num1[i]), int(num2[i]), int(num3[i]))))
        return int("".join(ans))
## 灵神题解
class Solution:
    def generateKey(self, x, y, z):
        ans = 0
        pow10 = 1
        while x and y and z:
            ans += min(x % 10, y % 10, z % 10) * pow10
            x //= 10
            y //= 10
            z //= 10
            pow10 *= 10
        return ans
	
if __name__ == '__main__':
	nums1 = 1
	nums2 = 2
	nums3 = 3
	cls = Solution()
	print(cls.generateKey(nums1, nums2, nums3))