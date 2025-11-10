import heapq
from collections import defaultdict
from heapq import heapify, heappush, heappop

# class TaskManager:

# 	def __init__(self, tasks):
# 		self.task_userId = defaultdict(int)
# 		self.new_task = []
# 		self.task_priority = defaultdict(int)
# 		self.remove_task = set()

# 		for userId, taskId, priority in tasks:
# 			self.task_userId[taskId] = userId
# 			self.task_priority[taskId] = priority
# 			heapq.heappush(self.new_task, (-priority, -taskId, userId))
# 			# self.new_task.append((-priority, -taskId, userId))

# 	def add(self, userId: int, taskId: int, priority: int):
# 		self.task_userId[taskId] = userId
# 		self.task_priority[taskId] = priority
# 		heapq.heappush(self.new_task, (-priority, -taskId, userId))
# 		# self.new_task.append((-priority, -taskId, userId))
# 		self.remove_task.remove(taskId)

# 	def edit(self, taskId: int, newPriority: int):
# 		self.task_priority[taskId] = newPriority
# 		userId = self.task_userId[taskId]
# 		heapq.heappush(self.new_task, (-newPriority, -taskId, userId))
# 		# self.new_task.append((-newPriority, -taskId, userId))

# 	def rmv(self, taskId: int):
# 		del self.task_priority[taskId]
# 		del self.task_userId[taskId]
# 		self.remove_task.add(taskId)

# 	def execTop(self) -> int:
# 		while self.new_task and -self.new_task[0][1] not in self.remove_task:
# 			priority, taskId, userId = heapq.heappop(self.new_task)
# 			if priority != self.task_priority[-taskId]:
# 				continue
# 			del self.task_priority[-taskId]
# 			del self.task_userId[-taskId]
# 			self.remove_task.add(-taskId)
# 			return userId
# 		return -1

class TaskManager:
    def __init__(self, tasks):
        self.mp = {taskId: (priority, userId) for userId, taskId, priority in tasks}
        self.h = [(-priority, -taskId, userId) for userId, taskId, priority in tasks]  # 取相反数，变成最大堆
        heapify(self.h)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (priority, userId)
        heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # 懒修改
        self.add(self.mp[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # 懒删除
        self.mp[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heappop(self.h)
            if self.mp[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
            # else 货不对板，堆顶和 mp 中记录的不一样，说明堆顶数据已被修改或删除，不做处理
        return -1

	
if __name__ == '__main__':
	s = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
	s.add(4,104,5)
	s.edit(102, 9)
	print(s.execTop())
	s.rmv(101)
	s.add(50,101,8)
	print(s.execTop())