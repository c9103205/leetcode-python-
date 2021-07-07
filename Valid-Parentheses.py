def isValid( s: str) -> bool:
    # trivial cases
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    return s == ''


if __name__ == "__main__":
    pass

# https://leetcode.com/problems/valid-parentheses/