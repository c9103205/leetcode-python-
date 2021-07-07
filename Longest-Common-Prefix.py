from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    firstWord = strs[0]
    temp =""
    # 要取得 index 必須這樣寫
    for str in strs:
        for k in range(len(str)):
            if str[k] == firstWord[k]:
                temp = temp + str[k]
            else :
                break


if __name__ == "__main__":
    strs =  ["flower","flow","flight"]
    longestCommonPrefix(strs)
