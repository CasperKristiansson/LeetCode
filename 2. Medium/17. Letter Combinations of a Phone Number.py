class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def combinations(index, combination):
            if len(digits) == 0:
                return
            
            if index == len(digits):
                result.append(combination)
                return
            
            for letter in phone_letters[digits[index]]:
                combinations(index+1, combination + letter)
        
        combinations(0, '')
        
        return result