from collections import Counter

class Solution:
	def minimumDeletions(self, word, k):
		word_dic = Counter(word)
		word_cnt_lis = sorted(list(cnt for cnt in word_dic.values()))
		ans = left = 0
		for right, c in enumerate(word_cnt_lis):
			while abs(c - word_cnt_lis[left]) > k:
				ans += word_cnt_lis[left]
				left += 1
		return ans

class Solution:
    def minimumDeletions(self, word, k):
        cnt = sorted(Counter(word).values())
        max_save = 0
        for i, base in enumerate(cnt):
            s = sum(min(c, base + k) for c in cnt[i:])  # 至多保留 base+k 个
            max_save = max(max_save, s)
        return len(word) - max_save

if __name__ == '__main__':
	word = "dabdcbdcdcd"
	k = 2
	print(Solution().minimumDeletions(word, k))