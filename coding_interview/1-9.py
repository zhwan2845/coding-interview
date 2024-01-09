# TODO: 1-9까지 풀어오기 (coding-interview-1)
def is_rotation(s1: str, s2: str) -> bool:
    """
    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a
    rotation of s1 using only one call to isSubstring
    """
    if len(s1) != len(s2):
        return False
    # else:
    #     for i in range(len(s1)):
    #         if s2[len(s2) - 1 - i] != s1[i]:
    #             return False

    s1s1 = s1 + s1
    if s2 in s1s1:
        return True
    else:
        return False

if __name__ == '__main__':
    # Write your test cases here
    assert is_rotation("waterbottle", "erbottlewat") == True
    assert is_rotation("waterbottle", "terbottlewa") == True
    assert is_rotation("waterbottle", "atlewaterbo") == False
    assert is_rotation("abc", "cab") == True
    assert is_rotation("abc", "bca") == True
    assert is_rotation("abc", "cba") == False
    assert is_rotation("hello", "world") == False
