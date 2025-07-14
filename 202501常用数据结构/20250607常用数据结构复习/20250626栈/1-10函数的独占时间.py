class Solution:
	def exclusiveTime(self, n, logs):
		logs = [list(info.split(':')) for info in logs]
		ans = [0]
		result = [0] * n
		st = []
		for id, tag, time in logs:
			id = int(id)
			time = int(time)
			if tag == 'end':
				st.pop()
				time += 1
				result[id] += time - ans[-1]
			else:
				if st:
					cur_id = st[-1]
					result[cur_id] += time - ans[-1]
				st.append(id)
			ans.append(time)
		return result
	
# class Solution:
#     def exclusiveTime(self, n: int, logs):
#         def helper(log):
#             idx, mark, time = log.split(":")
#             return int(idx), mark == "start", int(time)

#         stack, ans, total = [], [0] * n, 0
#         for lg in logs:
#             idx, is_start, time = helper(lg)
#             if is_start:
#                 stack.append((idx, time, total))
#             else:
#                 _, t, s = stack.pop()
#                 diff = time + 1 - t - total + s
#                 ans[idx] += diff
#                 total += diff
#         return ans

if __name__ == '__main__':
	n = 8
	logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
	print(Solution().exclusiveTime(n, logs))
