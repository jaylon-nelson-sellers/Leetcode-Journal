- [[1929. Concatenation of Array]]
- 
```
class Solution:

    def getConcatenation(self, nums: List[int]) -> List[int]:

        copy = nums

        nums += copy

        return nums
```

easy