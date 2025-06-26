from collections import defaultdict

class Solution1:
	def maximumBeauty(self, items, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		items_dic = defaultdict(int)
		for price, beauty in items:
			items_dic[price] = max(beauty, items_dic[price])

		ans = [0] * len(queries)
		item_price = list(items_dic.keys())
		item_price.sort()
		for i, querie in enumerate(queries):
			find = lower_bound(item_price, querie + 1)
			temp = 0
			for j in range(find):
				temp = max(temp, items_dic[item_price[j]])
			ans[i] = temp
		return ans

class Solution2:
	def maximumBeauty(self, items, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		items = sorted(items, key = lambda x:x[0])
		items_dic = defaultdict(int)
		pre_price = 0
		for price, beauty in items:
			pre_price = max(pre_price, beauty)
			items_dic[price] = pre_price
		ans = []
		item_price = list(items_dic.keys())
		for querie in queries:
			find = lower_bound(item_price, querie + 1) - 1
			if find == -1:
				ans.append(0)
			else:
				ans.append(items_dic[item_price[find]])
		return ans
## 灵神题解
class Solution2:
	def maximumBeauty(self, items, queries):
		items.sort(key = lambda item:item[0])
		for i in range(1, len(items)):
			items[i][1] = max(items[i][1], items[i - 1][1])

		for i, q in enumerate(queries):
			j = bisect_right(items, q, key = lambda item:item[0])
			queries[i] = items[j - 1][1] if j else 0
		return queries

if __name__ == '__main__':
	items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
	queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
	print(Solution2().maximumBeauty(items, queries))