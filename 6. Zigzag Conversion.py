class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        counter, dir = 0, 1
        result = []
        dictionary = {i: [] for i in range(numRows)}

        for i in range(len(s)):
            dictionary[counter].append(s[i])

            if counter == 0:
                dir = 1
            elif counter == numRows - 1:
                dir = 0

            if dir:
                counter += 1
            else:
                counter -= 1

        for value in dictionary.values():
            result.extend(value)

        return ''.join(result)