class Solution(object):
    def validMountainArray(self, arr):
        length = len(arr)
        current_pos = 0

        # 1. Climb up: Increment position while values are strictly increasing
        while current_pos + 1 < length and arr[current_pos] < arr[current_pos + 1]:
            current_pos += 1

        # 2. Validate Peak: The peak cannot be the first element (only descending) 
        # or the last element (only ascending).
        if current_pos == 0 or current_pos == length - 1:
            return False

        # 3. Walk down: Increment position while values are strictly decreasing
        while current_pos + 1 < length and arr[current_pos] > arr[current_pos + 1]:
            current_pos += 1

        # 4. Final Check: If we reached the end of the array, it's a valid mountain
        return current_pos == length - 1