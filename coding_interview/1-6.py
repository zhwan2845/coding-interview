#TODO: until 1/4
def compress(s: str) -> str:
    """
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become
    a2b1c5a3. If the "compressed" string would not become smaller than the
    original string, your method should return the original string.
    """
    cnt = 0
    new_s = ""
    for i in range(len(s)):
        cnt += 1

        # 다음 문자와 다를 때 또는 문자열이 끝날 때
        if (i + 1 >= len(s)) or (s[i] != s[i + 1]):
            # new_s.append(s[i] + str(cnt))
            new_s += s[i]
            new_s += str(cnt)
            cnt = 0

    # compressed_str = ''.join(compressed)
    return new_s if len(new_s) < len(s) else s

if __name__ == '__main__':
    # Write your test cases here
    s1 = "aabcccccaaa"
    s2 = "aaabc"
    s3 = "ab"
    assert compress(s1) == "a2b1c5a3"
    assert compress(s2) == "aaabc"
    assert compress(s3) == "ab"
