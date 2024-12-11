# 18.令牌放置
class Solution1:
	def bagOfTokensScore(self,token,power):
		token.sort()
		n=len(token)
		left,right=0,n-1
		ans=0
		max_ans=0
		while left<=right:
			if power>=token[left]:
				power-=token[left]
				ans+=1
				left+=1
				max_ans=max(max_ans,ans)
			else:
				if ans>0:
					power+=token[right]
					ans-=1
					right-=1
				else:
					break
		return max_ans
	
if __name__=='__main__':
	token=[100,200,300,400]
	power=200
	s=Solution1()
	print(s.bagOfTokensScore(token,power))