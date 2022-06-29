class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Resposta 1 - menor big O
        resposta = collections.defaultdict(list)
        
        for palavra in strs:
            key = [0] * 26
            for letra in palavra:
                key[ord(letra) - ord("a")] += 1
            resposta[tuple(key)].append(palavra)
        return resposta.values()
            
        # Resposta 2 
        sMap = {}
        
        for palavra in strs:
            sortedPalavra = str(sorted(palavra))
            if sortedPalavra in sMap:
                sMap[sortedPalavra].append(palavra)
            else:
                sMap[sortedPalavra] = [palavra]
                
        return sMap.values()