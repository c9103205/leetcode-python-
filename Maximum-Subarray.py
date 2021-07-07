
def maxSubArray( nums) -> int:
    sub = nums[0]
    total = 0
    for n in nums:
        if total < 0:
            total = 0
        total += n
        sub = max(total, sub)
    return sub


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))

# https://leetcode.com/problems/maximum-subarray/
