class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumDict = {}
        for i, j in enumerate(nums):
            temp = target - j
            if temp in NumDict:
                return [i, NumDict[temp]]
            NumDict[j] = i
