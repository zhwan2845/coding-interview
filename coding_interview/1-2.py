def is_permutation(s1: str, s2: str) -> bool:
    """
    Given two strings, write a method to decide if one is a permutation of the
    other.
    """
    if len(s1) == len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
    
    else:
        return False

if __name__ == '__main__':
    # Write your test cases here
    assert is_permutation("abcd", "bcda") == True
    assert is_permutation("shdf", "sdfg") == False
    assert is_permutation("opqr", "opqrs") == False