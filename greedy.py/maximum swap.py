class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        ans = num[:]
        for i, a in enumerate(num):
            for j,b in enumerate(num[i+1:],start=i+1):
                if a<b:
                    n=num[:]
                    n[i],n[j]=b,a
                    if n>ans:ans=n
        return int(''.join(ans))
