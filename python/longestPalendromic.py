# Given a string s, return the longest palindromic substring in s.

# Example:

# $ pSubstring('babad')
# $ 'bab' // or 'aba'

def pSubString(s: str):
    if not s:
        return ""
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            break
    return s[i:j+1]

if __name__ == "__main__":
    print(pSubString('babad'))