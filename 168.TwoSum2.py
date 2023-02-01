class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexFront = 0
        indexEnd = len(numbers) - 1
        while True:
            if numbers[indexFront] + numbers[indexEnd] == target:
                return [indexFront + 1, indexEnd + 1]
            elif numbers[indexFront] + numbers[indexEnd] > target:
                indexEnd -= 1
            elif numbers[indexFront] + numbers[indexEnd] < target:
                indexFront += 1