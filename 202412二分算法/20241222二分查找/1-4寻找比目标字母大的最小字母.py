# 4.寻找比目标字母大的最小字母
class Solution1:
	def nextGreatestLetter(self,letter,target):
		def lower_bound(letter,target):
			left = 0
			right = len(letter) - 1
			while left <= right:
				mid = (left + right) // 2
				if letter[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = lower_bound(letter,chr(ord(target) + 1))
		if ans == len(letter):
			return letter[0]
		else:
			return letter[ans]

if __name__ == '__main__':
	letter = ["e","e","g","g"]
	target = 'g'
	s = Solution1()
	print(s.nextGreatestLetter(letter,target))