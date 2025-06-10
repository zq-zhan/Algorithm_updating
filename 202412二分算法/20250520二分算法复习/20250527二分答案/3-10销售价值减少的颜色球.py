import heapq

class Solution1:
	def maxProfit(self, inventory, orders):
		mod = 10 ** 9 + 7
		inventory = [-x for x in inventory]
		heapq.heapify(inventory)
		ans = 0
		while orders > 0:
			x = heapq.heappop(inventory)
			heapq.heappush(inventory, 1 + x)
			ans += -x
			orders -= 1
		return ans % mod
	
class Solution:
    def maxProfit(self, inventory, orders):

        inventory.sort(reverse=True) #如果不reverse，就要从后往前遍历了
        sell = 0
        ans = 0

        def get(start,cnt,repeat,times): #处理不满的一轮
            ful,left = divmod(times,repeat)
            #并列项数的整数倍部分按照等差数列求和公式，余数乘上卖出整数倍之后的价值
            return (2*start-ful+1)*ful*repeat//2+(start-ful)*left 

        p = 0 
        while p<len(inventory):
            while p<len(inventory)-1 and inventory[p]==inventory[p+1]: #重复项合并处理
                p+=1
            #cnt为每种当前价值最高的球能卖出的数量，注意如果没有下一项，cnt就是当前项本身
            cnt = inventory[p]-inventory[p+1] if p<len(inventory)-1 else inventory[p] 

            if (p+1)*cnt+sell<=orders: #注意数组的下标从0开始，所以并列价值最高的项数是p+1
                #等差数列求和公式，尾项是是当前项减去cnt再加1，不要忘了乘上并列的数量
                ans=(ans+(2*inventory[p]-cnt+1)*(p+1)*cnt//2)%(10**9+7) 
                sell+=(p+1)*cnt
            else: 
                #这种情况对应这轮已经不满，这时可以直接return了
                return (ans+get(inventory[p],cnt,p+1,orders-sell))%(10**9+7)
            p+=1
        return ans #如果没有这一行，orders=sum(inventory)的情况就缺少返回值


## 二分法
class Solution:
    def maxProfit(self, inventory, orders):
        # 二分查找
        # 提示2：存在某个值k，其中所有价值大于k的球均卖出，部分（可能为0）价值为k的球卖出
        # 要想求出最大总价值和，应该让k尽可能小，这样在卖出一样球的情况下，k越小，所累加的价值就越高
        # 检查对于价值大于k的球的个数，是否超过orders，找到最小的k
        # 找到k之后，说明最初价值大于k的球都会卖出，卖的个数为(inventory[i]-k)，这部分球的卖出的价值可以用等差数列求和
        # ans += (inventory[i] + k + 1) * (inventory[i] - k) // 2 if inventory[i] > k
        # 剩下一部分价值为k的球（可能没有）需要卖出，才能够卖出orders，那么这部分球的个数rest = orders - sum
        # 这一部分球的价值和再加到最终答案中，ans += rest * k
        
        mod = 10**9+7
        l = 0
        r = max(inventory)
        while l <= r:
            mid = (l + r) >> 1
            # 假设价值大于mid的球全部卖出
            s = sum(x - mid for x in inventory if x > mid)
            # 如果价值大于mid的球的个数大于需要卖出的球的个数，说明这个k值应该更大才对
            if s > orders:
                l = mid + 1
            # 否则这个k值应该更小才对
            else:
                r = mid - 1
        k = l
        range_sum = lambda x, y : (x + y) * (y - x + 1) // 2
        rest = orders - sum(x - k for x in inventory if x > k)
        ans = 0
        for x in inventory:
            if x > k:
                ans += range_sum(k+1, x)
        ans += rest * k
        return ans % mod

if __name__ == '__main__':
	inven = [5, 3, 3, 2]
	orders = 10
	print(Solution().maxProfit(inven, orders))