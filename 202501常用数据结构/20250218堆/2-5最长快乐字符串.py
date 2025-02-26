# 12.最长快乐字符串
class Solution1:
	def longestDiverseString(self, a, b, c):
		n = a + b + c
		m = max(a, b, c)
		if m > (n - 1) // 2 + 1:
			return ''

		temp_dic = {'a':a, 'b':b, 'c':c}
		ans = [''] * n
		idx = 0
		for ch, cnt in temp_dic:
			for _ in range(cnt):
				ans[idx] = ch
				idx += 2
				if idx >= n:
					idx = 1
		return ''.join(ans)

## 参考解法
class Solution1:
	def longestDiverseString(self, a, b, c):
		ans = ''
		temp_dic = {'a':a, 'b':b, 'c':c}
		while True:
			# 动态获取当前剩余字符里三个字符
			less, mid, most = sorted(temp_dic.keys(), key = lambda x:temp_dic[x])
			if (len(ans) < 2 or not ans[-2] == ans[-1] == most) and temp_dic[most] > 0:
				ans += most
				temp_dic[most] -= 1
			elif (len(ans) >= 2 and not ans[-2] == ans[-1] == mid) and temp_dic[mid] > 0:
				ans += mid
				temp_dic[mid] -= 1
			else:
				return ans

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        题目要求：给定固定数量的字母a,b,c，返回一个尽可能长的字符串s，s满足最多有a个字母'a'、b个字母'b'、c个字母'c'且
                不含有任何'aaa''bbb'或'ccc' 这样的子串
        :param a: 给定字母a的数量
        :param b: 给定字母b的数量
        :param c: 给定字母c的数量
        :return: 返回满足要求的最长字符串
        """
        # 解题思路：题目本质很容易理解，仅使用不超过给定数量的字母a,b,c，构造出不能连续三个相同字母的字符串
        # 尽可能长，不能想到采用贪心策略，每次尽可能优先使用当前数量最多的字母，因为最后同一种字母剩余的越多，越容易出现字母连续相同的情况
        # 如果不满足条件，再使用剩余数量次多的字母，由于只有三种字母，实际上每次只会在数量最多和次多的字母中选择一个
        # 如果尝试所有的字母都无法使用，则直接结束，此时构成的字符串即为所求
        count = {'a': a, 'b': b, 'c': c}  # 初始化三种字母的数量
        res = ''  # 返回的结果字符串
        while True:
            _, mid, most = sorted(count.keys(), key=lambda x: count[x])  # 按照剩余数量排序，取出最多和次多的字母
            # 当最多的字母还有时，且结果字符串长度小于2或者最后两个字符不全为most，均可使用most
            if (len(res) < 2 or not res[-2] == res[-1] == most) and count[most]:
                res += most  # 接在结果后面
                count[most] -= 1  # 数量减一
            elif count[mid]:  # 否则使用次多的字母mid(进入这个elif,意味着结尾两个字符必然为most,故只需要mid字符还有就可以用)
                res += mid  # 接在结果后面
                count[mid] -= 1  # 数量减一
            else:  # 没有字母可以用了，结束
                break
        return res




if __name__ == '__main__':
	a = 0
	b = 0
	c = 1
	print(Solution2().longestDiverseString(a, b, c)) # Output: "ccaccb"
