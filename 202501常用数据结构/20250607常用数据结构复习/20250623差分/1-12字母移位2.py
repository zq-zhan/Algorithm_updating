from itertools import accumulate

class Solution:
	def shiftingLetters(self, s, shifts):
		n = len(s)
		new_arr = [0] * (n + 1)
		for start, end, direction in shifts:
			if direction:
				new_arr[start] += 1
				new_arr[end + 1] -= 1
			else:
				new_arr[start] -= 1
				new_arr[end + 1] += 1
		pre_s = list(accumulate(new_arr))
		ord_a = ord('a')
		s = list(s)
		for i in range(n):
			s[i] = chr((ord(s[i]) + pre_s[i] - ord_a) % 26 + ord_a)
		return ''.join(s)



if __name__ == '__main__':
	s = "abc"
	shifts = [[0,1,0],[1,2,1],[0,2,1]]
	print(Solution().shiftingLetters(s, shifts))