def urlify(s: str, length: int) -> str:
    """
    Write a method to replace all spaces in a string with '%20'. You may assume
    that the string has sufficient space at the end to hold the additional
    characters, and that you are given the "true" length of the string.
    """
    new_s = ""
    for i in s:
        if i == " ":
            new_s += "%20"
        else:
            new_s += i
    return new_s


if __name__ == '__main__':
    # Write your test cases here
    
    testcase = "abc d "
    result = "abc%20d%20"
    
    a = ""
    a += "abc"
    a += "de"
    # a = "abcde"
    print(urlify(testcase, len(testcase)))
