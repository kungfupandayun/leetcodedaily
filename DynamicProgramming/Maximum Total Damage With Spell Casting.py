class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c =Counter(power)
        l = list(c.keys())
        n= len(l)
        acc = [0]*n
        l.sort()

        for i,v in enumerate(l):
            acc[i]=v*c[v]
            j = i-1
            while j>=0:
                if l[i]-l[j]>2:
                    acc[i]+=acc[j]
                    break
                j-=1
            if i>=2:
                acc[i] = max(acc[i-2],acc[i-1],acc[i])
            if i ==1:
                acc[i] = max(acc[i-1],acc[i])
            

            
        return acc[n-1]
        