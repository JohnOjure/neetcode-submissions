class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        now_considering = None
        index = 0
        length = len(nums)

        for num in nums:
            now_considering = num
            print(f"{now_considering} -- {index}")


            # for i in range (index+1, length-1):
            #     if nums[i] == now_considering:
            #         return True

            for elem in nums[index+1:]:
                if elem == now_considering:
                    print("match found")
                    return True
            
            index += 1
        
        return False