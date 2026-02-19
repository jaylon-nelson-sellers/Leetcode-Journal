class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num = 0
        for n in nums:
            if n > 9 and n <100:
                even_num += 1
            elif n > 999 and n < 10000:
                even_num += 1
            elif n > 99999:
                even_num += 1

        return even_num