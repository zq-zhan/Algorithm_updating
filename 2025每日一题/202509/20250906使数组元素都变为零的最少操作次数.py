# class Solution:
# 	def minOperations(self, queries):
# 		ans = 0
# 		for start, end in queries:
# 			left = start
# 			right = end
# 			while left <= right:
# 				start //= 4
# 				end //= 4
# 				if start == 0:
# 					left += 1
# 					start = left
# 				if end == 0:
# 					right -= 1
# 					end = right
# 				ans += 1
# 		return ans

class Solution:
	def minOperations(self, queries):
		ans = 0
		for start, end in queries:
			temp_lis = [i for i in range(start, end + 1)]
			left, right = 0, end - start
			while left <= right:
				temp_lis[left] //= 4
				temp_lis[right] //= 4
				if temp_lis[left] == 0:
					left += 1
				if temp_lis[right] == 0:
					right -= 1
				ans += 1
		return ans

class Solution:
	def minOperations(self, queries):
		ans = 0
		for start, end in queries:
			left = start
			right = end
			while start <= end:
				left //= 4
				right //= 4
				if left == 0:
					start += 1
					left = start
				if right == 0:
					end -= 1
					right = end
				if start == end:
					left //= 4
					right //= 4
				ans += 1
		return ans

if __name__ == '__main__':
	queries = [[19,23]]
	print(Solution().minOperations(queries))