class Solution1:
	def trap(self, height):
		target_set = sorted(set(height))
		ans = 0
		temp_height = height.copy()
		left, right = 0, len(height) - 1
		for target in target_set:
			
			while left < right:
				while left < right and height[left] < target:
					left += 1
				while left < right and height[right] < target:
					right -= 1
				if left < right:
					break
			for i in range(left + 1, right):
				if temp_height[i] < target:
					ans += target - temp_height[i]
					temp_height[i] = target
		return ans

## 灵神题解
class Solution:
    def trap(self, height):
        ans = left = pre_max = suf_max = 0
        right = len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max <= suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans	

if __name__ == '__main__':
	# height = [4,2,0,3,2,5]
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	s = Solution()
	print(s.trap(height))