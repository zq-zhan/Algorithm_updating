class Solution1:
	def nextGreatestLetter(self, letters, target):
		def lower_bound(target):
			left, right = -1, len(letters)
			while left + 1 < right:
				mid = (left + right) // 2
				if letters[mid] < target:
					left = mid
				else:
					right = mid
			return right

		target = chr(ord(target) + 1)
		ans = lower_bound(target)
		if ans != len(letters):
			return letters[ans]
		else:
			return letters[0]
		
if __name__ == '__main__':
	letters = ["c", "f", "j"]
	target = "a"
	print(Solution1().nextGreatestLetter(letters, target))