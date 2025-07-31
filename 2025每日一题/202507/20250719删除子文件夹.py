class Solution:
	def removeSubfolders(self, folder):
		folder.sort(key = lambda x:len(x))
		set_win = set()
		ans = []
		for i, file_path in enumerate(folder):
			tag = False
			for path in set_win:
				n = len(path)
				if path in file_path and file_path[:n] == path and file_path[n] == '/':
					tag = True
					break
			if not tag:
				ans.append(i)
				set_win.add(file_path)
		return [folder[i] for i in ans]
	
if __name__ == '__main__':
	folder = ["/ah/al/am","/ah/al"]
	print(Solution().removeSubfolders(folder))
	
