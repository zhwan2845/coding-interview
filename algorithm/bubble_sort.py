from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    """
    Sort a list using the bubble sort algorithm.
    """
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    

if __name__ == '__main__':
    # Write your test cases here
    arr = [2, 4, 5, 1, 3]
    bubble_sort(arr)
    print(arr)