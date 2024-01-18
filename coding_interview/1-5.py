def is_one_away(s1: str, s2: str) -> bool:
    """
    There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two strings,
    write a function to check if they are one edit (or zero edits) away.
    """
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 - len_s2 == 0:
        return replace(s1, s2)
    elif len_s1 - len_s2 == 1:
        return remove(s1, s2)
    elif len_s1 - len_s2 == -1:
        return remove(s2, s1)
    else:
        return False

def replace(s1: str, s2: str) -> bool:
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
        if cnt == 2:
            return False
    return True

def remove(s1: str, s2: str) -> bool:
    i1 = 0
    i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            i1 += 1
        else:
            i1 += 1
            i2 += 1
        if i1 - i2 > 1:
            return False
    return True

if __name__ == '__main__':
    # Write your test cases here
    assert is_one_away("abcde", "abde") == True
    assert is_one_away("abd", "ab") == True
    assert is_one_away("abdef", "bbdef") == True
    assert is_one_away("zxy", "zxy") == True
    assert is_one_away("xyzer", "xyz") == False
    assert is_one_away("abcde", "axxde") == False
