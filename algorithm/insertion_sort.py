from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    """
    Sort a list using the insertion sort algorithm.
    """
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

if __name__ == '__main__':
    # Write your test cases here
    arr = [2, 4, 5, 1, 3]
    insertion_sort(arr)
    print(arr)