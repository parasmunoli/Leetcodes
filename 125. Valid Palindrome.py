def isPalindrome(s):
    str = ''.join(char.lower() for char in s if char.isalnum())
    return str == str[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))