from bisect import bisect_left
from collections import defaultdict

# class SnapshotArray:

# 	def __init__(self, length):
# 		self.arr = [0] * length
# 		self.nums = [self.arr]
# 		self.snap_id = 0


# 	def set(self, index, val):
# 		self.arr[index] = val
# 		self.nums[self.snap_id] = self.arr

# 	def snap(self):
# 		self.snap_id += 1
# 		self.nums.append(self.arr)
# 		return self.snap_id - 1

# 	def get(self, index, snap_id):
# 		return self.nums[snap_id][index]

class SnapshotArray:

	def __init__(self, length):
		self.nums_dic = defaultdict(list)
		self.snap_id = 0

	def set(self, index, val):
		self.nums_dic[index].append((self.snap_id, val))

	def snap(self):
		self.snap_id += 1
		return self.snap_id - 1

	def get(self, index, snap_id):
		find = bisect_left(self.nums_dic[index], (snap_id + 1,)) - 1
		if find == -1:
			return 0
		else:
			return self.nums_dic[index][find][1]
	
if __name__ == '__main__':
	s = SnapshotArray(1)
	s.set(0, 15)
	print(s.snap())
	print(s.snap())
	print(s.snap())
	print(s.get(0, 2))
	print(s.snap())
	print(s.snap())
	print(s.get(0, 0))
