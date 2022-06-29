class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers) - 1
        while i < j:
            soma = numbers[i] + numbers[j]
            if soma > target:
                j -= 1
            elif soma < target:
                i += 1
            else:
                return [i + 1, j + 1]