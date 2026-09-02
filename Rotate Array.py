def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

n, k = map(int, input().split())
nums = list(map(int, input().split()))

k %= n

reverse(nums, 0, n - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, n - 1)

print(*nums)
