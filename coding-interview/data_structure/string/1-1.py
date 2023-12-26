# 대소문자 구분 X
# "AaBb" -> False

# 딕셔너리 이용한 방법
def is_unique_characters(s: str) -> bool:
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """
    dic = {} # key-value
    s = s.lower()
    for i in range(len(s)):
        # key가 없으면 (처음 등장)
        if s[i] not in dic:
            dic[s[i]] = 1
        # key가 있으면 (중복)       
        else:
            return False
    return True

# 이중 for문 방법 (추가적인 자료구조 X) -> 시간복잡도 O(n^2)
def is_unique_characters_2(s: str) -> bool:
    s = s.lower() # 대문자 -> 소문자
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# 정렬하기 (추가적인 자료구조 X) -> 시간복잡도 O(nlogn)
def is_unique_characters_3(s: str) -> bool:
    s = s.lower()
    s = sorted(s)
    for i in range(1, len(s)): # 범위 설정 주의
        if s[i] == s[i - 1]:
            return False
    return True


if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "abcde" # True
    testcase2 = "AaBbCc" # False
    testcase3 = "" # True

    # Test `is_unique_characters` method
    assert is_unique_characters(testcase1) == True
    assert is_unique_characters(testcase2) == False
    assert is_unique_characters(testcase3) == True

    # Test `is_unique_characters_2` method
    assert is_unique_characters_2(testcase1) == True
    assert is_unique_characters_2(testcase2) == False
    assert is_unique_characters_2(testcase3) == True

    # Test `is_unique_characters_3` method
    assert is_unique_characters_3(testcase1) == True
    assert is_unique_characters_3(testcase2) == False
    assert is_unique_characters_3(testcase3) == True