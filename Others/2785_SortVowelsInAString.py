# Given s, permute s to get a new string t such that 
# all consonants remain the same position
# all vowels are sorted increasingly of their ASCII value
from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U',
                  'a','e','i','o','u']
        vow = Counter(s)
     
        pt = 0
        ans=""
        for i,c in enumerate(s):
            if c in vowels:
                found = False
                while not found:
                    if vow[vowels[pt]] > 0 :
                        ans+=vowels[pt]
                        vow[vowels[pt]] -=1
                        found = True
                    else:
                        pt+=1
            else:
                ans += s[i]
                
        return ans
            
            