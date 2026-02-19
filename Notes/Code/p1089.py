class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        @sum take arr and duplicate the zeroes in place. Additionally move non-zero values forward.
        @var arr: List[int] list of ints
        @constraints
            - 1 <= arr.length <= 104
            - 0 <= arr[i] <= 9

        @method: going forward and interating would be less effective.
        I use a forward and backward pass method. First pass counts zeros "arr.count"
        second pass moves backwards using those zeroes to place values
         
        """
        debug = False
        #forward pass
        zeroes_count = arr.count(0)
        size = len(arr)

        #backwards pass
        for i in range(size-1,-1,-1):
            if debug:
                print(arr[i])

            # if the value will fit in the arr [check for out of bounds]    
            if i + zeroes_count < size:
                arr[i+zeroes_count] = arr[i]
            # if the value is zero    
            if arr[i] == 0:
                #remove from count. important to do this first, as the previous if statement has already moved a zero
                zeroes_count -= 1
                #then place in arr if it fits
                if i + zeroes_count < size:                
                    arr[i+zeroes_count] = arr[i]
                    