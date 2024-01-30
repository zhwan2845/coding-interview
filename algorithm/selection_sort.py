from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """
    Selection sort on a list.
    """
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

if __name__ == '__main__':
    # Write your test cases here
    arr = [2, 4, 5, 1, 3]
    selection_sort(arr)
    print(arr)