def does_something(s):
    if len(s) != 11:
        return False
    for i in range(len(s)):
        if i < 3 or i == 4 or i == 5 or i > 6:
            if not s[i].isdigit():
                return False
        else:
            if s[i] != '-':
                return False
    return True
print(does_something("abc123"))
print(does_something("123-12-1234"))
print(does_something("111223333"))