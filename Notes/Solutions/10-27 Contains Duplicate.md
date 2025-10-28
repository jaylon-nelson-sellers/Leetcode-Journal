- [[217. Contains Duplicate]]

My Solution:
```
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        checks = {}

        for n in nums:

            if n in checks:

                return True

            else:

                checks[n] = True

        return False
```