# Given two string 's' and 't'
# return true if t is an anagram of s
# and false otherwise




# brute force approach
# Time complexity is O(n2)
def brute_force_anagram(s, t):
    for i in t:
        contains = False
        for j in s:
            if j == i:
                contains = True
        if contains is False:
            return False
    return True


string1 = "nagmara"
string2 = "anagram"

if brute_force_anagram(string1, string2):
    print(string2 + " is Anagram of " + string1)
else:
    print(string2 + " is not Anagram of " + string1)


# Optimal Approach
# Time Complexity is O(n)
# Space Complexity is O(1)
def anagram(s, t):
    if len(s) != len(t):
        return False

    charCounts = [0] * 26
    for i in range(len(s)):
        charCounts[ord(s[i]) - 97]  += 1
        charCounts[ord(t[i]) - 97] -= 1

    print("Yes" if all(x == 0 for x in charCounts) else "No")

anagram(string1, string2)