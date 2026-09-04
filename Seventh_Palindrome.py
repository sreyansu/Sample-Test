def seven_pali(n):
    arr = []
    pos = 0
    while len(arr) < 7:
        pos+=1
        left = n-pos
        right = n+pos
        temp_arr = []
        if left >= 10 and isPalindrome(left):
            temp_arr.append(left)
        if isPalindrome(right):
            temp_arr.append(right)
        temp_arr.sort(reverse = True)
        arr.extend(temp_arr)
    print(arr)
    res = arr[6]
    return res

def isPalindrome(num):
    if num<10:
        return False
    s = str(num)
    return s == s[::-1]

num=int(input())
print(seven_pali(num))
