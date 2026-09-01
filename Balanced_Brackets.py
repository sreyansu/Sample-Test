def isBalanced(s):
    stack = []
    mp = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != mp[ch]:
                return False
            stack.pop()
    return len(stack) == 0

s = input()
print(isBalanced(s))
