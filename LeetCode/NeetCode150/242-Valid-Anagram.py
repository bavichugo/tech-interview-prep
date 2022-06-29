class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        # Solucao 1
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        
        for letra in s:
            if letra in sMap:
                sMap[letra] += 1
            else:
                sMap[letra] = 1
        
        for letra in t:
            if letra in tMap:
                tMap[letra] += 1
            else:
                tMap[letra] = 1
                
        return sMap == tMap
    
        # Solucao 2
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        return sMap == tMap
        