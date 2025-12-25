class Solution:
	def countMentions(self, numberOfUsers, events):
		events.sort(key = lambda x:int(x[1]))
		ans = [0] * numberOfUsers
		offline_time = [-60] * numberOfUsers
		events_message = []
		events_offline = []
		for info, time, detail in events:
			if info == 'MESSAGE':
				events_message.append([info, int(time), detail])
			else:
				events_offline.append([info, int(time), int(detail)])
		idx_off = 0
		m = len(events_offline)
		for info, time, detail in events_message:
			while idx_off < m and events_offline[idx_off][1] <= time:
				offline_time[events_offline[idx_off][2]] = events_offline[idx_off][1]
				idx_off += 1
			if detail == "ALL":
				ans = [x + 1 for x in ans]
			elif detail == "HERE":
				for i in range(numberOfUsers):
					if offline_time[i] + 60 <= time:
						ans[i] += 1
			else:
				for idx in detail.split(' '):
					ans[int(idx[2])] += 1
			
		return ans



if __name__ == '__main__':
	numberOfUsers = 3
	events = [["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]]
	print(Solution().countMentions(numberOfUsers, events))