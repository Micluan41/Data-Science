import math
class Solution:
    def sortedSquares(selfself, nums):
        n=len(nums)
        neg=-1
        for i in range(n):
            if nums[i]<0:
                neg=i
            else:
                break
        result=[]
        left, right=neg, neg+1
        while left>=0 or right<n:
            if left<0:
                result.append(right*right)
                right+=1
            elif right==n:
                result.append(left*left)
                left-=1
            elif left*left<right*right:
                result.append(left*left)
                left-=1
            else:
                result.append(right*right)
                right+=1

        return result

nums=[-4,-1,0,3,10]
res=Solution()
print(res.sortedSquares(nums))