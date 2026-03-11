class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # We use a set for O(1) average time complexity lookups.
        # This allows us to check for the 'double' or 'half' in one pass.
        seen_numbers = set()

        for current_num in arr:
            # Condition 1: Does the double of this number exist? (e.g., current is 5, we saw 10)
            # Condition 2: Is this number even AND is its half already seen? (e.g., current is 10, we saw 5)
            # The 'current_num % 2 == 0' check ensures we don't look for floats (like 7 / 2 = 3.5)
            is_double = (2 * current_num in seen_numbers)
            is_half = (current_num % 2 == 0 and current_num // 2 in seen_numbers)

            if any([is_double, is_half]):
                return True
            
            # Add the current number to the set AFTER checking 
            # This naturally handles the "two zeros" requirement.
            seen_numbers.add(current_num)

        return False