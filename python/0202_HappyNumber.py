class Solution(object):
    def isHappy(self, n):
        return self.solve(n,{})
        
    def solve(self,n,v):
      if n == 1:
         return True
      if n in v:
         return False
      v[n]= 1
      n = str(n)
      l = list(n)
      l = list(map(int,l))
      t = 0
      for i in l:
         t += (i**2)
      return self.solve(t,v)
