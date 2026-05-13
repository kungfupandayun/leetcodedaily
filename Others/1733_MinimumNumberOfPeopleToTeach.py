# Social Network, m users , can communicate among if they know a common language
# Given integer n, array languages, array friendships
# Return the minimum users you need to teach so that all users can communicate with each other


 # 1. Find all pairs that do not have common language
 # 2. Find the most commonly spoken language among all users
 # 3. Count the users we taught the language to

class Solution:
   def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

      
      noCommonLanguageUser = set()
      for f in friendships:
         lp1 = set(languages[f[0]-1])
         lp2 = set(languages[f[1]-1])
         intersect = lp1.intersection(lp2)
         if len(intersect)==0:
            noCommonLanguageUser.add(f[0]-1)
            noCommonLanguageUser.add(f[1]-1)
      
      cnt = [0] * (n + 1)
      for c in noCommonLanguageUser:
         for l in languages[c]:
            cnt[l]+=1
            
      x=max(cnt)
      return len(noCommonLanguageUser) - x
      
      