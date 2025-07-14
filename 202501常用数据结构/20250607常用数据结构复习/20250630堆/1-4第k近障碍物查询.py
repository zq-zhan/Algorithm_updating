import heapq

class Solution:
	def resultsArray(self, queries, k):
		result = []
		new_arr = []
		heapq.heapify(new_arr)
		for x, y in queries:
			heapq.heappush(new_arr, -(abs(x) + abs(y)))
			while len(new_arr) > k:
				heapq.heappop(new_arr)
			if len(new_arr) < k:
				result.append(-1)
			else:
				result.append(-new_arr[0])
		return result
	
if __name__ == '__main__':
	queries = [[1, 2], [3,4],[2,3],[-3,0]]
	k = 2
	s = Solution()
	print(s.resultsArray(queries, k))