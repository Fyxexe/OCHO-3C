def sorting_for_encrypt_steep1(tokenText, n):
    for i in range(len(tokenText)):
        for j in range(len(tokenText[i]) - n):
            tokenText[i][j], tokenText[i][j + n] = tokenText[i][j + n], tokenText[i][j]
    return tokenText


def sorting_for_encrypt_steep2(tokenText: list[list[int]], n: int) -> list[list[int]]:
    encrypted_text = sorting_for_encrypt_steep1(tokenText, n)
    encrypted_result = []
    for i in encrypted_text:
        for j in i:
            encrypted_result.extend([j, j + n])
    return encrypted_result


def custom_encrypt(tokenText: list[list[int]], n: int) -> list[list[int]]:
    for i in range(len(tokenText)):
        for j in range(len(tokenText[i])):
            tokenText[i][j] += n
    return tokenText


def level2_encrypt(tokenText: list[list[int]]) -> list[list[int]]:
    for i in range(len(tokenText)):
        tokenText[i].reverse()
    return tokenText


def level3_encrypt(tokenText: list[list[int]]) -> list[list[int]]:
    for i in range(len(tokenText)):
        tokenText[i] = [x * 2 for x in tokenText[i]]
    return tokenText
