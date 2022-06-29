class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solucao 1
        i, j = 0, len(s) - 1
        
        while i <= j:
            if not s[i].isalpha():
                i += 1
                continue
            elif not s[j].isalpha():
                j -= 1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    
        # Solucao 2
        word = "".join([letra.lower() for letra in s if letra.isalpha()])
        i, j = 0, len(word) - 1
        
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True