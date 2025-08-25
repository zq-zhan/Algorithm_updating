from collections import defaultdict, deque

# class Solution:  # 超时
# 	def maxSlidingWindow(self, nums, k):
# 		ans = []
# 		n = len(nums)
# 		temp_win = defaultdict(int)
# 		left = 0
# 		for right, x in enumerate(nums):
# 			temp_win[x] += 1
# 			if right - left + 1 == k:
# 				ans.append(max(temp_win.keys()))
# 				if temp_win[nums[left]] == 1:
# 					del temp_win[nums[left]]
# 				else:
# 					temp_win[nums[left]] -= 1
# 				left += 1
# 		return ans
## 灵神题解——队列
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = [0] * (len(nums) - k + 1)  # 窗口个数
        q = deque()  # 双端队列

        for i, x in enumerate(nums):
            # 1. 右边入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)

            # 2. 左边出
            left = i - k + 1  # 窗口左端点
            if q[0] < left:  # 队首已经离开窗口了
                q.popleft()

            # 3. 在窗口左端点处记录答案
            if left >= 0:
                # 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans[left] = nums[q[0]]

        return ans
    
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))