def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    freq1 = {}
    freq2 = {}
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
    return freq1 == freq2

s1 = input()
s2 = input()
if anagram(s1, s2):
    print("The sentences are anagrams")
else:
    print("Not anagram")
