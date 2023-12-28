def is_palindrome(s: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word or phrase that is the same forwards and
    backwards. A permutation is a rearrangement of letters.
    """
    s = s.replace(" ", "")
    s = s.lower()
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

if __name__ == '__main__':
    # Write your test cases here
    assert is_palindrome("abcba") == True
    assert is_palindrome("abccba") == True
    assert is_palindrome("abcdef") == False
    assert is_palindrome("taco cat") == True
    assert is_palindrome("Tac cat") == True