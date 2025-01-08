# 1.正方形中的最多点数
class Solution1:
	def maxPointsInsideSquare(self, points, s):
		left = -1
		right = 0
		for i,point in enumerate(points):
			points[i] = [abs(x) for x in point]
			right = max(right, max(points[i]) * 2 + 1)

		def check(mid):
			n = len(s)
			ans = 0
			mark_lis = []
			for i,c in enumerate(s):
				if max(points[i]) <= mid //2:
					if c not in mark_lis:
						ans += 1
						mark_lis.append(c)
					else:
						return False, ans
				else:
					continue
			return True, ans
        
		ans = 0
		while left + 1 < right:
			mid = (left + right) // 2
			check_ans, temp = check(mid)
			if check_ans:
				left = mid
				ans = temp
			else:
				right = mid
		return ans
## 灵神思路
class Solution2:
	def maxPointsInsideSquare(self, points, s):
		ans = 0
		def check(size):
			vis = set()
			for (x, y), c in zip(points, s):
				if abs(x) <= size and abs(y) <= size:
					if c in vis:
						return False
					vis.add(c)
			nonlocal ans
			ans = len(vis)
			return True

		left = -1
		# right = 10 ** 9 + 1
		right = 0
		for i,point in enumerate(points):
			points[i] = [abs(x) for x in point]
			right = max(right, max(points[i]) * 2 + 1)

		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return ans
## 灵神题解
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ans = 0
        def check(size: int) -> bool:
            vis = set()
            for (x, y), c in zip(points, s):
                if abs(x) <= size and abs(y) <= size:  # 点在正方形中
                    if c in vis:
                        return True
                    vis.add(c)
            nonlocal ans
            ans = len(vis)
            return False
        # 注意 range 并不会创建 list，它是 O(1) 的
        bisect_left(range(1_000_000_001), True, key=check)
        return ans



