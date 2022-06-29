class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVal = {} # diferenca -> index
        
        for i, numero in enumerate(nums):
            diferenca = target - numero
            
            if numero in prevVal:
                return [prevVal[numero], i]
            prevVal[diferenca] = i
        