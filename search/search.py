from typing import List
class solution:
  def search(self, nums: List[int], target: int) -> int:
    left, right, mid = 0,len(nums)-1,0

    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
    return -1  