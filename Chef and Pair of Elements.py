def chef(nums,target):
    hashmap = {}
    for i,j in enumerate(nums):
        remaining = target - j
        if remaining in hashmap:
            return [hashmap[remaining],i]
        hashmap[j] = i
    return []

N = int(input())
nums = list(map(int,input().split()))
target = int(input())
print(chef(nums,target))
