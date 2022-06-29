class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        
        for numero in nums:
            if numero in hashSet:
                return True
            hashSet.add(numero)
        return False