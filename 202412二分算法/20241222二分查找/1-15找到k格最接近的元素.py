# 15.找到k格最接近的元素
from bisect import bisect_left

## 思路：二分法+双指针
class Solution:
    def findClosestElements(self, arr, k, x):
        idx = bisect_left(arr, x)
        left, right = idx - 1, idx
        res = []

        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            k -= 1
        
        return sorted(res)
	
if __name__ == '__main__':
	arr = [0,1,1,1,2,3,6,7,8,9]
	k = 9
	x = 4
	cls = Solution()
	print(cls.findClosestElements(arr,k,x))