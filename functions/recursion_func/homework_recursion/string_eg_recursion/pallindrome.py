# 4. Check Palindrome (VERY IMPORTANT)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
# Working ("MADAM")
# M == M → check "ADA"
# A == A → check "D"
# length 1 → True