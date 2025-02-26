# 4.在d天内送达包裹的能力
# 4.在d天内送达包裹的能力
class Solution1:
	def check(self, weights, mid, days):
		n = len(weights)
		left = 0
		cum_sum = 0
		cnt = 0
		while left < n:
			while left < n and cum_sum + weights[left] <= mid:
				cum_sum += weights[left]
				left += 1
			cum_sum = 0
			cnt += 1
		return cnt <= days

	def shipWithinDays(self, weights, days):
		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(weights, mid, days):
				right = mid
			else:
				left = mid
		return right
	
class Solution2:
    def shipWithinDays(self, weights, D):
        max_w, sum_w = max(weights), sum(weights)
        l, r = max(max_w, sum_w // D), sum_w
        while l < r:
            mid = (l + r) >> 1
            if self.check(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return r

    def check(self, ws, t, d):
        n = len(ws)
        i = cnt = 1
        total = ws[0]
        while i < n:
            while i < n and total + ws[i] <= t:
                total += ws[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d
	
class Solution3:
	def shipWithinDays(self, weights, days):
		def check(nums, target, days):
			ans = temp_sum = 0
			for x in nums:
				if temp_sum + x <= target:
					temp_sum += x
				else:
					ans += 1
					temp_sum = x
			if temp_sum <= target:
				ans += 1
			return ans <= days


		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(weights, mid, days):
				right = mid
			else:
				left = mid
		return right


if __name__ == '__main__':
	weights = [1,2,3,1,1]
	days = 4
	s = Solution3()
	print(s.shipWithinDays(weights, days))