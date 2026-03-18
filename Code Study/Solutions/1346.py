class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for i in arr:
          # if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
            if 2 * i in seen or float(i) / 2 in seen:
                return True
            seen.add(i)
        return False