class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        abs_values_arr = [0] * size

        end_of_arr = size -1
        start_of_arr = 0

        for i in range(size):
            if abs(nums[start_of_arr]) > abs(nums[end_of_arr]):
                abs_values_arr[i] = abs(nums[start_of_arr])
                start_of_arr += 1
            else:
                abs_values_arr[i] = abs(nums[end_of_arr])
                end_of_arr -= 1
        
        #print(abs_values_arr)
        final_squared_arr = [0] * size
        j = 0
        for i in range(size-1,-1,-1):
            final_squared_arr[j] = abs_values_arr[i] ** 2
            j += 1

        return final_squared_arr