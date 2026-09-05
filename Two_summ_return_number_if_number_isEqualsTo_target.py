def two_sum(num,target):
    hashmap = {}
    for ind,number in enumerate(num):
        if number == target:
            return ind
        complement = target - number
        if complement in hashmap:
            return [hashmap[complement],ind]
        hashmap[number] = ind
num = [9,4,10,20,60,2,-100]
target = int(input())
print(two_sum(num,target))
