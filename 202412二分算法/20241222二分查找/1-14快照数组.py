# 14.快照数组
from bisect import bisect_left,bisect_right
from collections import defaultdict

# class SnapshotArray:
# 	def __init__(self, length):
# 		self.arr = [0] * length
# 		self.cnt = -1
# 		self.snap_arr = []
# 		self.nums = []
		

# 	def set(self, index, val):
# 		self.arr[index] = val

# 	def snap(self):
# 		self.cnt += 1
# 		self.nums.append(self.cnt)
# 		self.snap_arr.append(self.arr.copy())
# 		return self.cnt

# 	def get(self, index, snap_id):
# 		nums = self.nums
# 		find = bisect_left(nums, snap_id)
# 		if find > self.cnt:
# 			return ''
# 		else:
# 			return self.snap_arr[find][index]

## 灵神思路:记录添加修改的快照编号和val
class SnapshotArray:
	def __init__(self, length):
		self.cur_snap_id = 0
		self.history = defaultdict(list)  # 每个index的历史修改记录,甚至都不需要原数组，因为不存在0直接返回0

	def set(self, index, val):
		self.history[index].append((self.cur_snap_id, val))

	def snap(self):
		self.cur_snap_id += 1
		return self.cur_snap_id - 1

	def get(self, index, snap_id):
		# 找快照编号<=snap_id的最后一次修改记录
		find = bisect_left(self.history[index], (snap_id + 1,)) - 1
		if find == -1:
			return 0
		else:
			return self.history[index][find][1]
		
if __name__ == '__main__':
	s = SnapshotArray(3)
	s.set(0, 5)
	s.snap()
	s.set(0, 6)
	print(s.get(0,0))
	# s.set(0, 1)
	# s.set(1, 2)
	# s.set(2, 3)
	# s.snap()
	# s.set(0, 4)
	# s.set(1, 5)
	# s.set(2, 6)
	# s.snap()
	# s.set(0, 7)
	# s.set(1, 8)
	# s.set(2, 9)
	# s.snap()
	# print(s.get(0,0))
	# print(s.get(0,1))
	# print(s.get(0,3))
	# print(s.get(3,1))