from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        unique_tuples = set()
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            seen = {}  # dictionary/map
            for j in range(i + 1, n):
                # find pair that sums to -cur
                complement = target - nums[j]
                if complement in seen:  # and j != map[complement]:
                    unique_tuples.add(tuple(sorted([nums[i], nums[j], complement])))
                else:
                    seen[nums[j]] = j

        print(f"result_set: {unique_tuples}")
        unique_lists = [list(tpl) for tpl in unique_tuples]
        return unique_lists
        '''

        # two pointers approach
        result = []
        nums.sort()

        for i in range(len(nums)):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # avoid duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


obj = Solution()
res = obj.threeSum([-1,0,1,2,-1,-4])
print(f"result: {res}")
